    #include<bits/stdc++.h>
    #include<string>
    using namespace std;
    typedef long long ll;
    typedef long double ld;
    typedef pair<ll,ll > pii;
    typedef pair<long,pii > piii;
    typedef vector<long long >   VI;
    #define sc1(x) scanf("%lld",&x);
    #define sc2(x,y) scanf("%lld%lld",&x,&y);
    #define sc3(x,y,z) scanf("%lld%lld%lld",&x,&y,&z);
    #define pb push_back
    #define mp make_pair
    #define ini(x,val) memset(x,val,sizeof(x));
    #define fs first
    #define sc second
    #define MOD 1000000007
    #define inf 999999999999999ll	//long long inf
    #define PI 3.1415926535897932384626

    #define gcd __gcd
    #define tr(contaner, it)  for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)
    #define PrintCont(cont) {cout<<("\n----------------\n");\
    for(typeof(cont.begin()) it = cont.begin();it!=cont.end();++it) cout<<*it<<" ";cout<<("\n----------------\n");}
    #define all(v) v.begin(),v.end()
    #define fast_io ios_base::sync_with_stdio(false);cin.tie(NULL)

    #define debug(x) cout<<#x<<" :: "<<x<<"\n";
    #define debug2(x,y) cout<<#x<<" :: "<<x<<"\t"<<#y<<" :: "<<y<<"\n";
    #define debug3(x,y,z) cout<<#x<<" :: "<<x<<"\t"<<#y<<" :: "<<y<<"\t"<<#z<<" :: "<<z<<"\n";

    int main()
    {
        //freopen("input.txt","r",stdin);
        //freopen("out.txt","w",stdout);
        ll t,cas=0;
        cin>>t;
        while(t--)
        {
            cas++;
            string str,str1,str2;
            ll ans,cnt1=0,cnt2=0,k,n;
            cin>>str>>k;
            n=str.length();
            str1=str;
            str2=str;
            cnt1=0;
            for(int i=0;i<n;i++)
            {
                if(str1[i]=='-'&&i+k-1<n)
                {
                    cnt1++;
                    for(int j=i;j<i+k;j++)
                    {
                        if(str1[j]=='-')
                        {
                            str1[j]='+';
                        }
                        else
                        {
                            str1[j]='-';
                        }
                    }
                }
            }
            for(int i=0;i<n;i++)
            {
                if(str1[i]=='-')
                {
                    cnt1=inf;
                }
            }
            //sec
            cnt2=0;
            for(int i=n-1;i>=0;i--)
            {
                if(str2[i]=='-'&&i-k+1>=0)
                {
                    cnt2++;
                    for(int j=i;j>=i-k+1;j--)
                    {
                        if(str2[j]=='-')
                        {
                            str2[j]='+';
                        }
                        else
                        {
                            str2[j]='-';
                        }
                    }
                }
            }
            for(int i=0;i<n;i++)
            {
                if(str2[i]=='-')
                {
                    cnt2=inf;
                }
            }
            //dsfd
            ans=min(cnt1,cnt2);
            cout<<"Case #"<<cas<<": ";
            if(ans==inf)
            {
                cout<<"IMPOSSIBLE"<<endl;
            }
            else
            {
                cout<<ans<<endl;
            }
        }
        return 0;
    }