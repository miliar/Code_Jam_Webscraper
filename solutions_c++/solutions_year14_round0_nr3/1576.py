// import the CP library. 
// replace cpsolver by cotfd if you use and older version of comet
import cpsolver;
// create the CP Solver 

string path = "/home/francois/Documents/Comet/compiler/CO/in";
ifstream file(path);

int nt = file.getInt();

forall(t in 1..nt) {

	cout << "Case #" << t << ":" << endl;

	Solver<CP> cp();

	int h = file.getInt();
	int w = file.getInt();
	int M = file.getInt();

	if(M == h * w - 1) {
		forall(i in 1..h) {
			forall(j in 1..w) {
				if(i == 1 && j == 1) {
					cout << "c";
				} else {
					cout << "*";
				}
			}
			cout << endl;
		}
		continue;
	}

	// 0 = empty
	// 1 = empty but adjacent to mine
	// 2 = mine

	var<CP>{int} x[1..h, 1..w](cp, 0..2);
	var<CP>{int} m[1..h, 1..w](cp, 0..1);
	var<CP>{int} ci(cp, 1..h);
	var<CP>{int} cj(cp, 1..h);
	
	Integer sol(0);

	solveall<cp> {
		// the c is at an empty position
		forall(i in 1..h, j in 1..w)
			cp.post((i == ci && j == cj) => x[i, j] == 0);
		// there are exactly M mines
		cp.post(sum(i in 1..h, j in 1..w) m[i, j] == M);
		// if there is a mine at ij then the type of x[i,j] is 2
		forall(i in 1..h, j in 1..w)
			cp.post(m[i, j] == 1 => x[i, j] == 2);
		// if there is no mine at ij then the type of x[i,j] is either 0 or 1
		forall(i in 1..h, j in 1..w)
			cp.post(m[i, j] == 0 => x[i, j] < 2);
		// if there is a mine at ij then all adjacent cells either contain a mine of are adjacent to a mine
		forall(i in 1..h, j in 1..w)
			cp.post(x[i, j] == 2 => prod(di in -1..1, dj in -1..1 : (di != 0 || dj != 0) && 1 <= i + di && i + di <= h && 1 <= j + dj && j + dj <= w) x[i + di, j + dj] != 0);
		// if ij is adjacent to a mine then ther exists an empty adjacent position
		forall(i in 1..h, j in 1..w)
			cp.post(x[i, j] == 1 => prod(di in -1..1, dj in -1..1 : (di != 0 || dj != 0) && 1 <= i + di && i + di <= h && 1 <= j + dj && j + dj <= w) x[i + di, j + dj] == 0);
	} using {
		label(cp);
		// check connectivity of the solution
		bool vis[1..h, 1..w] = false;
		vis[ci, cj] = true;
		queue{int} qi();
		queue{int} qj();
		qi.enqueueBack(ci);
		qj.enqueueBack(cj);
		while(qi.getSize() > 0) {
			int i = qi.dequeueFront();
			int j = qj.dequeueFront();
			forall(di in -1..1, dj in -1..1 : (di != 0 || dj != 0) && 1 <= i + di && i + di <= h && 1 <= j + dj && j + dj <= w && x[i + di, j + dj] == 0 && !vis[i + di, j + dj]) {
				qi.enqueueBack(i + di);
				qj.enqueueBack(j + dj);
				vis[i + di, j + dj] = true;
			}
		}
		bool ok = true;
		forall(i in 1..h, j in 1..w) {
			if(x[i, j] == 0 && !vis[i, j]) {
				 ok = false;
			}
		}
		// print solution if connectivity ok
		if(ok) {
			forall(i in 1..h) {
				forall(j in 1..w) {
					if(m[i, j] == 1) {
						cout << "*";	
					} else if(i == ci && j == cj) {
						cout << "c";
					} else {
						cout << ".";
					}
				}
				cout << endl;
			}
			sol := 1;
			cp.exit();
		}
	}

	if(sol == 0) {
		cout << "Impossible" << endl;
	}

}



