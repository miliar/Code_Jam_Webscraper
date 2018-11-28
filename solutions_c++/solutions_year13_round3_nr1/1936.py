#include <iostream>
#include <vector>
#include <set>
#define mp(a,b) make_pair((a),(b))
#define pii pair <int,int> 

using namespace std;

int vowel(char c)
{
    if(c=='a' || c=='e' || c=='i' || c=='o' || c=='u')
    return 1;
    return 0;
}

int main()
{
    freopen("C1.txt","rt",stdin);
    freopen("C1out.txt","wt",stdout);
    int TN,TC=1;
    cin >> TN;cin.get();
    for(;TC<=TN;TC++)
    {
                     string s;
                     int n,l;
                     cin >> s;
                     l=s.size();
                     cin >> n;
                     cin.get();
                     int i,j,k;
                     int ans=0;
                     for(i=0;i<l;i++)
                     for(j=i;j<l;j++)
                     {
                                     int cons=0;
                                     for(k=i;k<=j;k++)
                                     {
                                                      if(!vowel(s[k]))
                                                      cons++;
                                                      else
                                                      cons=0;
                                                      if(cons==n)
                                                      {
                                                                 ans++;
                                                                 break;
                                                      }
                                     }
                     }
                     cout << "Case #" << TC << ": " << ans << endl;
                     
    }
}
                                                      
                                                      
                                     
                                     
