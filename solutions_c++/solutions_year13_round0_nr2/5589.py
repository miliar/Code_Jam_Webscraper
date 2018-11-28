#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>
#include <map>
#include <cmath>
#include <algorithm>
#include <set>
#include <stack>




using namespace std;





int main(){

	freopen("me.in","r",stdin);
	freopen("he.out","w",stdout);

	int cases;
	scanf("%d",&cases);
	for(int i=1;i<=cases;i++){


		int row,col;
		scanf("%d %d",&row,&col);

		int arr[row][col];
		for(int j=0;j<row;j++){

			for(int k=0;k<col;k++){

				scanf("%d",&arr[j][k]);
			}

		}

		bool uni=false;
		bool flag1=false,flag2=false;
		for(int j=0;j<row;j++){

			for(int k=0;k<col;k++){

				if(arr[j][k]==1){
					flag1=false;
					flag2=false;


					for(int nn=0;nn<col;nn++){
						if(arr[j][nn]==2){
							flag1=true;
						}
					}

					for(int nn=0;nn<row;nn++){

						if(arr[nn][k]==2){
							flag2=true;
						}
					}




					if(flag1 && flag2 ){
						uni=true;
						break;
					}


				}

			}
		}
		if(uni){
			printf("Case #%d: NO\n",i);
		}
		else
		{
			printf("Case #%d: YES\n",i);
		}

	}



}

