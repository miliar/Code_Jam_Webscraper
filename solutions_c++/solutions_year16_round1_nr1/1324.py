  #include<iostream>
  #include<cstdio>
  #include<algorithm>
  #include<vector>
  #include<string>
  #include<map>
  #include<queue>
  #include<cmath>
  #include<stack>
  #include<sstream>
  #include<list>


  using namespace std;


  typedef long long ll;
  typedef long l;

  #define floop(i,n) for(ll i=0;i<n;i++)
  #define floopk(i,n,k) for(ll i=0;i<n;i+=k)
  #define si(n) scanf("%ld",&n)
  #define po(n) printf("%ld",n)



  int main()
  {
      //std::ios_base::sync_with_stdio(false);
      freopen("A-large.in","r",stdin);
      freopen("output_large_a.txt","w",stdout);

      l t;
      cin>>t;
      for(l f=1;f<=t;f++){
        string str;
        cin>>str;
        char arr[1001];
        char xx[1001];
        l ind=0,x=0;
        l len=str.length();
        arr[ind]=str[0];
        for(l i=1;i<len;i++){
                if(arr[ind]<=str[i]){
                    ind++;
                    arr[ind]=str[i];
                }
                else
                {
                    xx[x]=str[i];
                    x++;

                }

        }
        cout<<"Case #"<<f<<": ";
        for(int i=ind;i>=0;i--)
            cout<<arr[i];
        for(int j=0;j<x;j++)
            cout<<xx[j];
        cout<<"\n";
      }


      return 0;
  }








