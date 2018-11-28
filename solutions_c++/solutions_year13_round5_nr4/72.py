#include <iostream> 
#include <sstream> 
#include <vector> 
#include <set> 
#include <map> 
#include <algorithm> 
#include <string> 
#include <iomanip>
#include <cstring> 

using namespace std; 

int ttt, tttt;

double M[1 << 21];
int n,i,q,num,j,tmp;
int w[22];
string s;

int main(){
    freopen("d1.dat","r",stdin);
    freopen("d1.sol","w",stdout);
    cin >> ttt;
    for (tttt=1;tttt<=ttt;tttt++){
        cout << "Case #" << tttt << ": ";
        
        cin >> s;
        n = s.size();
        q = 0;
        for (i=0;i<n;i++)
            if (s[i] == 'X') (q = q | (1 << i));
            
            
        memset(M,0,sizeof(M));
        cout << fixed << setprecision(15);
        
        for (i=(1 << n)-2;i>=0;i--){
            for (j=0;j<n;j++)
                if (i & (1 << j)) w[j] = 1; else w[j] = 0;
                
            tmp = 0;
            while (w[tmp] == 1) tmp++;
            num = tmp;
            
            for (j=n-1;j>=0;j--){
                if (w[j] == 0){
                         tmp = 0;
                         M[i] += (M[i ^ (1 << j)]+n)/n;
                         num = j;
                } else {
                       tmp++;
                       M[i] += (M[i ^ (1 << num)]+n-tmp)/n;
                }
            }
        }
            
        cout << M[q] << endl;
        
    }
//    system("pause");
    return 0;
}

 
