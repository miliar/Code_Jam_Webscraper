#include<iostream>

using namespace std;



main()
{
	int t,tt,x,r,c;
	int mat_blocks;

	cin>>tt;
	t=1;
	string op[tt];
	int z=0;
	while(t<=tt){

		cin>>x>>r>>c;
		
		if(x==1 || (x==2 && ((r*c)%2)==0) || (x == 3 && ((r*c)>=(x*2))  && ((r*c)%3==0) ) || 
		(x >= 4  &&  ( ((r >= x) && (c>=(3))) || ((c >= x) && (r>=(3))) ) && x<=6  && ((r*c)%x==0) )  ) {
            		op[z++]="GABRIEL";
        	}else
            		op[z++]="RICHARD";

		t++;
	}

	cout<<endl;
	int i=0;
	while(i< z)
		cout<<"Case #"<<i<<": "<<op[i++]<<endl;






}



