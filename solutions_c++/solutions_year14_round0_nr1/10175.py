#include<iostream>
#include<fstream>
#include<string>
#include<conio.h>

using namespace std;

int n,m,mem;
int a[4];
int ch;

int main()
{
    ofstream fout ("a.out");
    ifstream fin ("a.in");

    fin >> m;
    for (int i = 1; i <= m; i++)
    {
        fin >> n;
        for(int j = 0; j < 4; j++) {
            if (j == n-1) {
                for(int k = 0; k < 4; k++) {
                    fin >> a[k];
                }
            } else {
                for(int k = 0; k < 4; k++) {
                    fin >> ch;
                }
            }
        }

        fin >> n;
        int count = 0;
        for(int j = 0; j < 4; j++) {
            if (j == n-1) {
                for(int k = 0; k < 4; k++) {
                    fin >> ch;
                    for(int l = 0; l < 4; l++)
                        if(ch == a[l]) {
                            mem = ch;
                            count++;
                        }
                }
            } else {
                for(int k = 0; k < 4; k++) {
                    fin >> ch;
                }
            }
        }
        
        fout << "Case #" << i << ": ";
        if (count == 1) {
            fout << mem;
        } else if(count > 1) {
            fout << "Bad magician!";
        } else {
            fout << "Volunteer cheated!";
        }
        
        if (i < m) {
            fout << endl;
        }
    }
    return 0;
}
