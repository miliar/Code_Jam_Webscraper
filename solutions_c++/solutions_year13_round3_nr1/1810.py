#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;


bool check(char a)
{
    if (a=='a' || a=='e' || a=='i' || a=='o' || a=='u') {
        return true;
    }
    else
    {
        return false;
    }
}

int main()
{
     freopen("1in.txt", "r", stdin);
    freopen("1output.txt", "w", stdout);
    int tc; scanf("%d\n", &tc);
    for(int g = 0; g < tc; g++) {
        int count = 0;
        string s;
        cin>>s;
        int m;
        cin>>m;
        int n = s.length();
        for (int i = 0; i<n-m+1;i++ ) {
            for (int j = m; j<n-i+1; j++) {
                bool flag = false;
                string buff = s.substr(i,j);
                for (int k = 0; k<j-m+1; k++) {
                    bool flagin = true;
                    for (int l = 0; l<m; l++) {
                        if (check(buff[k+l])) {
                            flagin = false;
                            break;
                        }
                      
                    }
                    if (flagin == true) {
                        flag = true;
                        break;
                    }
                    
                }
                if (flag == true) {
                    count++;
                }
            }
            
            
        }
    cout<<"Case #"<<g+1<<": "<<count<<endl;
    }


return 0;
}
