#include <bits/stdc++.h>

using namespace std;

void fill(string& str, int n) {
    for (int i = 0; i < n; ++i) {
        str[i] = '.';
    }
}

int main() {
    string infile, outfile;
    cin>>infile;
    outfile = infile + ".out";

    ifstream in(infile.c_str());
    ofstream out(outfile.c_str());

//    istream& in = cin;
//    ostream& out = cout;

    int T;

    in>>T;
    for (int cas = 1; cas <= T; ++cas) {
        int r, c, m;
        in>>r>>c>>m;
        out<<"Case #"<<cas<<":\n";
        bool flag = false;
        if (r > c ) {
            flag = true;
            swap(r, c);
        }
        int n = r * c - m;
        vector<string> graph(r, string(c, '*'));

        try {
            if (n == 1) {
                graph[0][0] = '.';
            }
            else if (r == 1) {
                fill(graph[0], n);
            }
            else if (r == 2) {
                if (n < 4 || (n & 1)) throw 1;
                else {
                    fill(graph[0], n / 2);
                    fill(graph[1], n / 2);
                }
            }
            else {
                if (n >= 3 * c) {
                    for (int i = 0; i < n / c; ++i)
                        fill(graph[i], c);
                    if (n % c) fill(graph[n / c], n % c);
                    if (n % c == 1) {
                        graph[n / c][1] = '.';
                        graph[n / c - 1].back() = '*';
                    }
                }
                else {
                    if (n < 4 || n == 5 || n == 7) {
                        throw 1;
                    }
                    if (!(n & 1)) {
                        if (n <= 2 * c) {
                            fill(graph[0], n / 2);
                            fill(graph[1], n / 2);
                        }
                        else {
                            fill(graph[0], c);
                            fill(graph[1], c);
                            fill(graph[2], n - 2 * c);
                        }
                    }
                    else {
                        if (n >= 9) {
                            fill(graph[0], (n - 3) / 2);
                            fill(graph[1], (n - 3) / 2);
                            fill(graph[2], 3);
                        }
                    }
                }
            }
        }
        catch(int) {
            out<<"Impossible"<<endl;
            continue ;
        }
        graph[0][0] = 'c';
        if (flag) {
            vector<string> old_graph = graph;
            swap(r, c);
            graph = vector<string>(r, string(c, '*'));
            for (int i = 0; i < r; ++i) {
                for (int j = 0; j < c; ++j) {
                    graph[i][j] = old_graph[j][i];
                }
            }
        }
        for_each(graph.begin(), graph.end(), [&out](const string&line){ out<<line<<endl;});
    }

/*
    if (file != "std") {
        fclose(in), fclose(out);
    }
    getchar();
    */
    return 0;
}
