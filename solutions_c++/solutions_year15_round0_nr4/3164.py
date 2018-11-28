#include<iostream>

using namespace std;



main()
{
	int T,TT,x,r,c;
	int mat_blocks;
	string players[2];
	players[0]="RICHARD";
 	players[1]="GABRIEL";	

	//read x ominoes rows and columns
	cin>>TT;
	T=1;
	int output_arr[TT];
	int output_index=0;
	while(T<=TT){
	
		cin>>x>>r>>c;
		
		if(x==1) {
            		output_arr[output_index++]=1;
        	}else if(x==2 && ((r*c)%2)==0){
            		output_arr[output_index++]=1;

        	}else if(x == 3 && ((r*c)>=(x*2))  && ((r*c)%3==0) ){
           		output_arr[output_index++]=1;


        	}else if(x >= 4  &&  ( ((r >= x) && (c>=(3))) || ((c >= x) && (r>=(3))) ) && x<=6  && ((r*c)%x==0)   ){
            		output_arr[output_index++]=1;


        	}else
            		output_arr[output_index++]=0;

		


		T++;
	}


	//print answers
	cout<<endl;
	int i=0;
	while(i< output_index)

		cout<<"Case #"<<i<<": "<<players[output_arr[i++]]<<endl;






}



