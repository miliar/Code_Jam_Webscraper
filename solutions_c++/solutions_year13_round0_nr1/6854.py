#include<iostream>
using namespace std;
int main(){
		int t,i,j,arr[4][4],sum1=0,sum2=0,sum3=0,sum4=0,emp=0,n;
		char ch;
		cin>>t;
		n = t;
		int o_flg=0,x_flg=0,drw_flg=0,in_flg=0;
		while(t--){
			
			for(i=0;i<4;i++){
				for(j=0;j<4;j++){
					cin>>ch;
					if (ch =='X')             // x ==1
					arr[i][j] = 1;
					else if(ch == 'O')
					arr[i][j] = 50;
					else if(ch == 'T')
					arr[i][j] = 0;
					else
					arr[i][j] = -1;
				}
			}
			/////////////////////////////////////////////
			for(i =0;i<4;i++){
				for(j=0;j<4;j++){
					
 					if(arr[i][j] == -1)
            emp = 1;

          sum1 += arr[i][j];
					sum2 += arr[j][i];
					if(i == j)
					sum3 += arr[i][i];
					if( i+j == 3)
					sum4 += arr[i][j];

				}
				if(sum1 == 150 || sum2 == 150 || sum1 == 200 || sum2 == 200){
				o_flg = 1;
				}
				else if(sum1 == 3 || sum2 == 3 || sum1 == 4 || sum2 == 4){
				x_flg = 1;
				}
				sum1 = 0;sum2 =0;
			}
			if(sum3 == 150 || sum4 == 150 || sum3 == 200 || sum4 == 200)
			o_flg = 1;
			else if(sum3 == 3 || sum4 == 3 || sum3 == 4 || sum4 == 4)
			x_flg = 1;
      else if(emp == 0 && x_flg == 0 && o_flg == 0)
			drw_flg = 1;
			else if(emp == 1 && x_flg == 0 && o_flg == 0)
			in_flg = 1;
			
			if(o_flg == 1)
			cout<<"Case #"<<n-t<<": O won"<<endl;
			if(x_flg == 1)
			cout<<"Case #"<<n-t<<": X won"<<endl;
      if(drw_flg == 1)
			cout<<"Case #"<<n-t<<": Draw"<<endl;
			if(in_flg == 1)
			cout<<"Case #"<<n-t<<": Game has not completed"<<endl;
      
      cout<<endl;
		  o_flg = 0;x_flg = 0;drw_flg = 0;in_flg = 0;emp=0;sum1 = 0;sum2 = 0;sum3 = 0;sum4 = 0;//reset	
		}
}
