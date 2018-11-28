//#include <bits/stdc++.h>
//using namespace std;
//typedef long long LL;
//typedef long double LD;
//typedef unsigned long long ULL;
//typedef pair<int, int> PI;
//typedef pair<PI, PI > PII;
//const double eps=1e-5;
//const LL mod=1e9+7;
//const double pi=acos(-1.0);
//const int MAXN=201000;
//const int MAXM=299900;
//const int N=1e6+5;
//bool sign[1500000];
//int n;
//string answer;
//int main()
//{
//    while(scanf("%d",&n)!=EOF)
//    {
//        int temp=(1<<n)-1;
//        memset(sign,false,sizeof(sign));
//        answer.clear();
//        sign[temp]=true;
//        answer.insert(0,n,'1');
//        while(temp--)
//        {
//            int ans=0;
//            for(int i=answer.length()-n+1; i<answer.length(); i++)
//                ans=ans<<1+answer[i]-'0';
//            int ans1=ans<<1;
//            if(!sign[ans1])
//            {
//                sign[ans1]=true;
//                answer+='0';
//            }
//            else
//            {
//                sign[ans1+1]=true;
//                answer+='1';
//            }
//        }
//        cout<<answer<<endl;
//    }
//    return 0;
//}

#include <bits/stdc++.h>
using namespace std;
int main()
{
    freopen("C:/Users/Kewowlo/Desktop/1.in","r",stdin);
    freopen("C:/Users/Kewowlo/Desktop/2.out","w",stdout);
    int t,cas=1;
    cin>>t;
    while(t--)
    {
        __int64 n,y=0;
        set<int>st;
        cin>>n;
        printf("Case #%d: ",cas++);
        if(n==0){

            puts("INSOMNIA");
            continue;
        }

        while(st.size()!=10)
        {
            y++;
            __int64 x = n*y;
            while(x)
            {
                st.insert(x%10);
                x/=10;
            }
        }
        cout<<y*n<<endl;
    }
    return 0;
}
