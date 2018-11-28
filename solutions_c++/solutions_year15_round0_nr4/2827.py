typedef long long ll;
#include <iostream>
using namespace std;
int main()
{
	ll t,x,c,r,w=1;
	bool result;
	cin>>t;
	while(t--)
	{
		result=false;
	cin>>x>>c>>r;
	switch(x)
	{
		case 4:
			 if((r==3 && c==4)||(r==4 && c==3)||(r==4 && c==4))
            result=true;
            break;
        case 3:
        	 if((r==2 && c==3)||(r==3 && c==2)||(r==3 && c==4)||(r==4 && c==3)||(r==3 && c==3))
            result=true;
            break;
         case 2:
	         if((r==1 && c==1)||(r==1 && c==3)||(r==3 && c==1)||(r==3 && c==3))
	            result=false;
	            else
	            result=true;
	            break;
		case 1:
		result=1;
		break;	
	}
   cout<<"Case #"<<w++<<": ";
   if(result)
   cout<<"GABRIEL"<<endl;
   else
    cout<<"RICHARD"<<endl;
}
return 0;
}
