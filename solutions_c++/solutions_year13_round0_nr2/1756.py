#include<iostream>
#include<fstream>
#include<queue>
using namespace std;
const int MAX_N = 100;

int lawn[MAX_N+1][MAX_N+1];
bool lawnadd[MAX_N+1][MAX_N+1][MAX_N+1];
typedef pair< pair<int, int>, int > tpos;

class tpos_comp{
public:
  bool operator() (const tpos& lhs, const tpos& rhs) const
  {
    return (lhs.second>rhs.second);
  }
};

int count, n, m, a;

int go_hoz(tpos & p) {
    bool fits = true;
            for(int y = p.first.first; y <= n; y++)
                if ((lawn[y][p.first.second] != -1)&&
                    (lawn[y][p.first.second] != p.second)) {
                        fits = false;
                        break;
                    }
            if (fits)
                for(int y = p.first.first; y <= n; y++)
                    lawn[y][p.first.second] = -1;
            /*if (fits)
                cout << p.second << p.first.first << p.first.second << endl;
            for(int y = 1; y <= n; y++) {
                cout << endl;
                for(int x = 1; x <= m; x++)
                    cout << lawn[y][x] << " ";
            }
            cout << endl;*/
}


int go_vert(tpos & p) {
    bool fits = true;
            for(int x = p.first.second; x >= 1; x--)
                if ((lawn[p.first.first][x] != -1)&&
                    (lawn[p.first.first][x] != p.second)) {
                        fits = false;
                        break;
                    }
            if (fits)
                for(int x = p.first.second; x >= 1; x--)
                    lawn[p.first.first][x] = -1;
/*if (fits)
                cout << p.second << p.first.first << p.first.second << endl;
            for(int y = 1; y <= n; y++) {
                cout << endl;
                for(int x = 1; x <= m; x++)
                    cout << lawn[y][x] << " ";
            }
            cout << endl;*/
}

int compute(char *txt, char *txt2) {
	ifstream fin(txt);
	ofstream fout(txt2);

	fin >> count;
	for(int i = 1; i <= count; i++) {
        fin >> n >> m;
        for(int y = 1; y <= n; y++)
            for(int x = 1; x <= m; x++)
                for(int h = 0; h <= 100; h++)
                    lawnadd[y][x][h] = false;
        priority_queue<tpos, vector<tpos>, tpos_comp > que;
        tpos p;
        for(int y = 1; y <= n; y++)
            for(int x = 1; x <= m; x++) {
                fin >> a;
                lawn[y][x] = a;
                if (!lawnadd[1][x][a]) {
                    p.first.first = 1;
                    p.first.second = x;
                    p.second = a;
                    que.push(p);
                    lawnadd[1][x][a] = true;
                }
                if (!lawnadd[y][m][a]) {
                    p.first.first = y;
                    p.first.second = m;
                    p.second = a;
                    que.push(p);
                    lawnadd[y][m][a] = true;
                }
            }

        while(!que.empty()) {
            p = que.top();
            if (p.first.first == 1)
                go_hoz(p);
            if (p.first.second == m)
                go_vert(p);
            que.pop();
        }

        fout << "Case #" << i << ": ";
        int rez = true;
        for(int y = 1; y <= n; y++) {
            for(int x = 1; x <= m; x++)
                if (lawn[y][x] != -1) {
                    rez = false;
                    break;
                }
            if (!rez)
                break;
        }
        if (rez)
            fout << "YES" << endl;
        else
            fout << "NO" << endl;
        /*fout << endl << "Case " << i << endl;
        for(int y = 1; y <= n; y++) {
            fout << endl;
            for(int x = 1; x <= m; x++)
                fout << lawn[y][x] << " ";
        }
        fout << endl;*/

        /*

        while(!que.empty()) {
            cout << que.top().second << endl;
            que.pop();
        }*/

	}


    fout.close();
	fin.close();
}

int main(int argc, char* argv[]) {
	compute((char*)("input.txt"), (char*)("output.txt"));
	return 0;
}
