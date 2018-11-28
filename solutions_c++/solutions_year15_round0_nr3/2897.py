#include<iostream>
#include<stdio.h>
#include<cstring>
#include<stdlib.h>
#include <queue>
#include<string>
#include <sstream>
#include<list>
#include<map>
#include<cmath>
#include<algorithm>

using namespace std;

bool negative;
char quaternion (char first, char second)
{
	negative = false;
	if(first == '1') 
		return second;

	if(first == 'i')
	{
		if(second == '1') 
			return 'i';
		else if(second == 'i') {
			negative = true;
			return '1';
		}
		else if(second == 'j') {
			return 'k';
		}
		else if(second == 'k') {
			negative = true;
			return 'j';
		}
	}
	else if(first == 'j')
	{
		if(second == '1') 
			return 'j';
		else if(second == 'i') {
			negative = true;
			return 'k';
		}
		else if(second == 'j') {
			negative = true;
			return '1';
		}
		else if(second == 'k') {
			return 'i';
		}
	}
	else if(first == 'k')
	{
		if(second == '1') 
			return 'k';
		else if(second == 'i')
			return 'j';

		else if(second == 'j') {
			negative = true;
			return 'i';
		}
		else if(second == 'k') {
			negative = true;
			return '1';
		}
	}
	//return '0';//without value !!
}
char str[10002];
int main()
{
	int	flag = 0,n,i=0,j,index = 0,x,y,m,input,sum,ans;

	freopen ("d:/Codejam/C-small-attempt3.in","r",stdin);
	freopen ("d:/Codejam/C-small-attempt3.out","w",stdout);
	scanf("%d",&input);

	char ch ='i',c='j',d='k';
	int L,X;

	while(input--)
	{

		scanf("%d%d",&L,&X);
		scanf("%s",&str);
		int flag =1,X_Y_Z_1='1',positive=1;	
		bool is_neg=false;
		for(int times=1;times<=X;times++){
			for(i=0;i<L;i++){

				X_Y_Z_1 =quaternion(X_Y_Z_1,str[i]);//'x','y','z'

				if(negative==false && is_neg==true)//anyone false
					is_neg=true;
				else if(negative==true && is_neg==false)
					is_neg = true;
				else
					is_neg = false;

				if(flag<3){//not yet i,j,k found
					if(is_neg == false){
						if(flag==1 && X_Y_Z_1 =='i'){//i found !!! :)
							flag=2;
							X_Y_Z_1='1';//reset
							
						}
						else if(flag==2 && X_Y_Z_1 =='j'){//j found !!! :)
							flag=3;
							X_Y_Z_1='1';
							
						}
						//else if(flag==3 && X_Y_Z_1 =='k'){//k found !!! :)
						//flag++;
						//X_Y_Z_1='1';
						//}
					}

				}
			}
		}
		printf("Case #%d: ",++index);

		if(is_neg ==false && flag == 3 && X_Y_Z_1=='k' )
			cout<<"YES\n";
		else
			cout<<"NO\n";
	}
	return 0;
}
