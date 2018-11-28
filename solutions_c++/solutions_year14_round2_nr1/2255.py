             /*
     shubham_1286(shubham verma)
                                   */
#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<iostream>
#include<vector>
#include<deque>
#include<map>
#include<set>
#include<stack>
#include<queue>
#include<algorithm>
#include<list>
#include<deque>
#include<bitset>
#include<limits.h>
#include<sstream>
#define max(x,y) x>y?x:y
#define min(x,y) x<y?x:y
#define sd(a)  scanf("%d",&a);
#define slld(a)  scanf("%lld",&a);
#define sllu(a)  scanf("%llu",&a);
#define pd(a)  printf("%d\n",a);
#define plld(a)  printf("%lld\n",a);
#define pllu(a)  printf("%llu\n",a);
#define inf INT_MAX
#define low INT_MIN
#define mod 1000000009
#define ull unsigned long long
#define ll long long
using namespace std;
vector<string>vec;
string s;
int main()
{
// freopen("c:\\users\\verma\\desktop\\aa1.txt","r",stdin);
//freopen("c:\\users\\verma\\desktop\\out1.txt","w",stdout);
 
  int t,test=1;
  sd(t);
  while(test<=t)
  {
        int n;
        sd(n);
        
        for(int i=0;i<n;i++)
        {
            cin>>s;
            vec.push_back(s);
        }
        sort(vec.begin(),vec.end());
      //  for(int i=0;i<n;i++)
        //cout<<vec[i]<<endl;
        
        int h=0,k=0,x=0,y=0,first=0,second=0,ans=0;
        bool temp=true;
        for(int i=0;i<n-1;i++)
        {
            x=0;y=0;
            first=0;second=0;
            while(first<vec[i].length() || second <vec[i+1].length())
            {
            //cout<<vec[i][first]<<vec[i+1][second]<<endl;;
           // cout<<i<<" "<<first<<" "<<second<<endl;
            x=0;y=0;
            if(vec[i][first]==vec[i+1][second])
            {
                for(int j=first;j<vec[i].length();j++)
                {
                    if(vec[i][j]==vec[i][j+1])
                       {
                            first++;x++;}
                       else
                       break;
                }
                
                 for(int j=second;j<vec[i+1].length();j++)
                {
                    //cout<<vec[j]<<" "<<vec[j+1]<<endl;
                    if(vec[i+1][j]==vec[i+1][j+1])
                       {second++;y++;}
                       else
                       break;
                }
        //        cout<<"first :"<<first<<" "<<"second :"<<second<<" "<<i<<x<<" "<<y<<endl;
                if(abs(x-y)>0)
                    ans+=abs(x-y);
               }
               else
               {
                     printf("Case #%d: %s\n",test,"Fegla Won");
                     temp=false;
                     break;
                }
                first+=1;second+=1;
              //  cout<<x<<" "<<y<<endl;
      //cout<<ans<<endl;
        }
        //cout<<"ss"<<endl;
    }
                  if(temp)
                 printf("Case #%d: %d\n",test,ans);
                vec.clear();
                test++;
                
                
                
            }
 
 
 // system("pause");
 }
