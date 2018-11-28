#include<iostream>
using namespace std;
int main()
{
    int T,i,j,X,R,C,res=0,t1=1,temp,flag=0;
    cin >> T;
    while(T--)
    {
        cin >> X >> R >> C;
        flag=0;



					if((R*C)%X==0){
						if(R>=X||C>=X){
							temp=0;
							//int flag=0;/// gabrial wins
							if(R>=X){
								temp=C;
							}else{
								temp=R;
							}
							if(X==3){
								if(temp<=1){
									flag=1;
								}
							}else if(X==4){
								if(temp<=2){
									flag=1;
								}
							}
							if(flag==0){
								//writer.printf("GABRIEL");
								flag=0;
							}else{
								flag=1;
								//writer.printf("RICHARD");
							}
						}else{
							flag=1;
							//writer.printf("RICHARD");
						}
					}else{
						flag=1;
						//writer.printf("RICHARD");
					}





        if(flag==0)
         cout << "Case #" << t1 <<": " << "GABRIEL" << endl;
         else
         cout << "Case #" << t1 <<": " << "RICHARD" << endl;

         t1++;

    }

    return 0;
}

