# include <iostream>
# include <vector>
# include <cmath>
using namespace std;

bool palindrome(int x)
{
     vector<int> v;
     while(x != 0){
     
             v.push_back(x % 10);
             x = x/10;
     }
     
     for (int i = 0; i < v.size()/2; i++){
         if(v[i] != v[v.size()-1-i]){
                 return false;
         }
     }
     return true;
}
         
int main()
{
    int t;
    cin >> t;
    
    for (int i = 0; i < t; i++){
        int a,b;
        cin >> a >> b;
        
        int k = sqrt(a);
        int m = sqrt(b);
        int cnt = 0;
        for (int j = k;j  <= m; j++){
            if((j * j  >= a) && (j *j  <= b)){
                  if(palindrome(j) && palindrome(j*j)){
                                   cnt++;
                  }
            }
        }
        cout << "Case #" << i+1 <<": "; 
        cout << cnt << endl;
    }
    
    return 0;
}
