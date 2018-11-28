#include<iostream>
using namespace std;
int main()
{ int T,t;
cin>>T;
for(t=1;t<=T;t++)
{ int k,c,s,i;
 cin>>k>>c>>s;
 if(k==1)
 { cout<<"Case #"<<t<<": "<<1<<endl; continue; }
 if(c==1)
  { cout<<"Case #"<<t<<":";
   if(s>=k)
   { for(i=1;i<=k;i++)
      cout<<" "<<i;
      cout<<endl;
	  continue;
   }
   else
   cout<<" IMPOSSIBLE"<<endl;
   }
 else
 { cout<<"Case #"<<t<<":";
   if(k%2)
    {  if(s>=k/2+1)
	   {  for(i=1;i<k;i+=2)
            cout<<" "<<(i-1)*k+i+1;
             cout<<" "<<(i-3)*k+i<<endl;
        }
        else
        cout<<" IMPOSSIBLE"<<endl;
    } 
else
   { if(s>=k/2)
     { for(i=1;i<=k;i+=2)
	     cout<<" "<<(i-1)*k+i+1;
		 cout<<endl;
	 }
	 else
	  cout<<" IMPOSSIBLE"<<endl;
   }
}
}
}
   
    