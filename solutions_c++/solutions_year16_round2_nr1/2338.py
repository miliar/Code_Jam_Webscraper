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
      for(int k=1;k<=t;k++){
        map<char,l> mp;
        string str;
        cin>>str;

        int arr[10];
        for(int i=0;i<10;i++)
            arr[i]=0;
        l len=str.length();
        for(l i=0;i<len;i++)
            mp[str[i]]++;

        l tp=0;
        tp=mp['Z'];
        mp['Z']-=tp;mp['E']-=tp;mp['R']-=tp;mp['O']-=tp;
        arr[0]=tp;

        tp=0;
        tp=mp['W'];
        mp['T']-=tp;mp['W']-=tp;mp['O']-=tp;
        arr[2]=tp;

        tp=0;
        tp=mp['U'];
        mp['F']-=tp;mp['U']-=tp;mp['O']-=tp;mp['R']-=tp;
        arr[4]=tp;

        tp=0;
        tp=mp['X'];
        mp['S']-=tp;mp['I']-=tp;mp['X']-=tp;
        arr[6]=tp;

        tp=0;
        tp=mp['G'];
        mp['E']-=tp;mp['I']-=tp;mp['G']-=tp;mp['H']-=tp;mp['T']-=tp;
        arr[8]=tp;

         tp=0;
        tp=mp['F'];
        mp['E']-=tp;mp['I']-=tp;mp['F']-=tp;mp['V']-=tp;
        arr[5]=tp;

        tp=0;
        tp=mp['V'];
        mp['E']-=(2*tp);mp['S']-=tp;mp['N']-=tp;mp['V']-=tp;
        arr[7]=tp;

         tp=0;
        tp=mp['O'];
        mp['E']-=tp;mp['O']-=tp;mp['N']-=tp;
        arr[1]=tp;


        tp=0;
        tp=mp['R'];
        mp['E']-=(2*tp);mp['T']-=tp;mp['H']-=tp;mp['R']-=tp;
        arr[3]=tp;

        tp=0;
        tp=mp['I'];
        mp['N']-=(2*tp);mp['I']-=tp;mp['E']-=tp;
        arr[9]=tp;


        cout<<"Case #"<<k<<": ";
        for(int i=0;i<=9;i++){
            for(int j=0;j<arr[i];j++)
                cout<<i;
        }
        cout<<"\n";







      }






      return 0;
  }








