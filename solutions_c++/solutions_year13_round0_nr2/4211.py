// This is written in vala, if you can't recognize the language

// This program makes use of glib functions
// http://ftp.acc.umu.se/pub/gnome/sources/glib/

const string uri = "B-large.in";

const string sample = "5
3 3
2 1 2
1 1 1
2 1 2
5 5
2 2 2 2 2
2 1 1 1 2
2 1 2 1 2
2 1 1 1 2
2 2 2 2 2
1 3
1 2 1
3 3
2 1 2
3 1 3
2 1 2
5 2
2 2
2 2
2 2
2 1
2 2";

bool mow (int[,] s){
	var nb = new bool[s.length[0]];
	var mb = new bool[s.length[1]];

	for (int i = 0; i < nb.length; i++)
		nb[i] = false;
	for (int i = 0; i < mb.length; i++)
		mb[i] = false;

	for (int num = 1; num <= 100; num++){
		bool notfinished = true;
		while (notfinished){
			notfinished = false;
			for (int n = 0; n < nb.length; n++){
				if (nb[n])
					continue;
				bool good = true;
				//int num = -1;
				for (int m = 0; m < mb.length; m++){
					if (mb[m])
						continue;
					/*if (num == -1)
						num = s[n, m];
					else */if (s[n,m] != num){
						good = false;
						break;
					}
				}
				nb[n] = good;
				notfinished = notfinished || good;
			}

			for (int m = 0; m < mb.length; m++){
				if (mb[m])
					continue;
				bool good = true;
				//int num = -1;
				for (int n = 0; n < nb.length; n++){
					if (nb[n])
						continue;
					/*if (num == -1)
						num = s[n, m];
					else */if (s[n,m] != num){
						good = false;
						break;
					}
				}
				mb[m] = good;
				notfinished = notfinished || good;
			}
		}
	}

	for (int i = 0; i < s.length[0]; i++){
		for (int j = 0; j < s.length[1]; j++){
			if (nb[i] || mb[j])
				continue;
			return false;
			//stdout.printf ("%i ", s[i,j]);
		}
		//stdout.printf ("\n");
	}

	return true;
}

void run (DataInputStream d, FileStream o) {
	int numlines = int.parse (d.read_line ());
	for (int casenum = 0; casenum < numlines; casenum++){
		string c = d.read_line ();

		string[] nm = c.split (" ");
		int n = int.parse (nm[0]);
		int m = int.parse (nm[1]);

		var lawn = new int[n, m];

		for (int i = 0; i < n; i++){
			string[] s = d.read_line ().split (" ");
			for (int j = 0; j < m; j++){
				lawn[i,j] = int.parse (s[j]);
				//stdout.printf ("%i ", lawn[i,j]);
			}
			//stdout.printf ("\n");
		}

		bool ret = mow (lawn);

		o.printf("Case #%i: %s\n", casenum + 1, ret ? "YES" : "NO");
	}
}

int main () {
	if (uri == ""){
		// testing
		var input = new MemoryInputStream.from_data (sample.data, null);
		var d = new DataInputStream (input);
		run (d, stdout);
	} else {
		// run
		var o = FileStream.open ("./" + Log.FILE + ".res", "w");
		var input = File.new_for_path (uri);
		var d = new DataInputStream (input.read ());
		run (d, o);
	}
	return 0;
}
