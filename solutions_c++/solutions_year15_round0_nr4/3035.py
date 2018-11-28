#include<bits/stdc++.h>
    #include<string>
    using namespace std;
    template< class T > T gcd(T a, T b) { return (b != 0 ? gcd<T>(b, a%b) : a); }
    template< class T > T lcm(T a, T b) { return (a / gcd<T>(a, b) * b); }
    #define traverse(container, it) \
      for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)
    #define         mp(mul, y) make_pair(mul, y)
    #define         SIZE(c) (int)c.size()
    #define         pb(mul) push_back(mul)
    //#define       map<char,int>::iterator it;
    #define         ff first
    #define         ss second
    #define         ll long long
    #define         ld long double
    #define         pii pair< int, int >
    #define         psi pair< string, int >
    #define         p(n) printf("%d\n",n)
    #define         p64(n) printf("%lld\n",n)
    #define         s(n) scanf("%d",&n)
    #define         s64(n) scanf("%I64d",&n)
    #define         rep(i,a,b) for(i=a;i<b;i++)
    #define         MOD (1000000007ll)



int main(){
	int t,x,r,c;



freopen("D-small-attempt1.in", "r", stdin);
    //freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin>>t;



	int k=1;






	while(t--){
			   cin>>x>>r>>c;


			   if(x==4)
				{
				if((r==3 && c==4)|| (r==4 && c==3) || (r==4 && c==4))
				{cout<<"Case #"<<k<<": "<<"GABRIEL"<<endl;
				  k++;continue;
				 }
				else
				 {cout<<"Case #"<<k<<": "<<"RICHARD"<<endl;
				  k++;continue;
				}
		 }



			   if(x==1){cout<<"Case #"<<k<<": "<<"GABRIEL"<<endl;
				  k++;continue;
				 }

			   if(x==2)
			   {

				 if( (r==1 && c==3)||(r==1 && c==1)  || (r==3 && c==1) || (r==3 && c==3))
				{cout<<"Case #"<<k<<": "<<"RICHARD"<<endl;
				  k++;continue;
				 }
				 else{cout<<"Case #"<<k<<": "<<"GABRIEL"<<endl;
				  k++;continue;
				 }


				}
				if(x==3)
				{
				if(  (c==2 && r==2)||(r==1 || c==1) ||(r==4 && c==2) || (r==4 && c==4)|| (r==2 && c==4))
				{


				    cout<<"Case #"<<k<<": "<<"RICHARD"<<endl;


				  k++;
				  continue;
				 }
				else
				{

				    cout<<"Case #"<<k<<": "<<"GABRIEL"<<endl;



				  k++;continue;
				 }

				}


}


return 0;
}
