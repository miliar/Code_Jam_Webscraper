#include <bits/stdc++.h>
#include <fstream>
using namespace std;
int main()
{
    //ofstream myfile;
    //myfile.open("output2.txt");
    int tc;
    scanf("%d\n", &tc);
    for(int ncase = 0; ncase < tc; ncase++)
    {
        int n;
        string s;
        scanf("%d ", &n);
        cin >> s;

        int standing = 0;
        int result = 0;
        for(int i = 0; i < n; i++)
        {
            standing += (s.at(i)-48);
            if(standing < i+1 && s.at(i+1)-48 != 0){
                    result+=i+1-standing;
                    standing += i+1-standing;
            }
        }

        cout << "Case #"<<ncase+1<<": " << result << endl;
    }
    //myfile.close();
}
