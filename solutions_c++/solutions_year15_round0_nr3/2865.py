  #include<iostream>
  #include<stdio.h>
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
    l cal(l a,l b){
        if(b==1 )
            return a;

         if(a==b)
            return -1;

         if(-a==b)
            return 1;

        if(a==1)
            return b;
        if(a==-1)
            return -b;



        if(a==105 && b==106)
            return 107;
        if(a==105 && b==107)
            return -106;
        if(a==106 && b==105)
            return -107;
        if(a==106 && b==107)
            return 105;
        if(a==107 && b==105)
            return 106;
        if(a==107 && b==106)
            return -105;
        if(a==-105 && b==106)
            return -107;
        if(a==-105 && b==107)
            return 106;
        if(a==-106 && b==105)
            return 107;
        if(a==-106 && b==107)
            return -105;
        if(a==-107 && b==105)
            return -106;
        if(a==-107 && b==106)
            return 105;

    }


  int main()
  {
      //std::ios_base::sync_with_stdio(false);
      l t;
       freopen("C-small-attempt1.in","r",stdin);
      freopen("sol.txt","w",stdout);
      si(t);
      for(l v=1;v<=t;v++){
            l n,f;
            si(n);si(f);
            char ch[n+1];
            cin>>ch;
            l prev=1,prev1=1,prev2=1,mychar=105,ind=f;
            floop(b,n){
                prev1=cal(prev1,ch[b]);
            }
            //cout<<prev1<<"\n";
            floop(p,f){
                floop(x,n){
                    l val=ch[x];
                    //cout<<prev<<"\n";
                    prev=cal(prev,val);

                    if(prev==mychar){
                        mychar++;
                        prev=1;
                    }

                }
                if(mychar==108){
                    ind=p;
                    break;
                }





            }
           // cout<<prev<<"\n";

            for(l w=ind+1;w<f;w++){
                    if(prev1<0)
                       prev=-(cal(prev,-prev1));
                    else
                        prev=cal(prev,prev1);
            }
            //cout<<prev<<"\n";
            if(mychar==108 && prev==1)
                cout<<"Case #"<<v<<": "<<"YES\n";
            else
                cout<<"Case #"<<v<<": "<<"NO\n";



      }


      return 0;
  }







