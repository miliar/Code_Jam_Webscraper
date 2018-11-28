#include<bits/stdc++.h>

int cal(char input[]){
	int size1 =strlen(input);

	int i1,i3,arr[size1],number[10];

	for(i1=0;i1<=9;i1++){
		number[i1]=0;
	}

	for(i1=0;i1<size1;i1++){
		arr[i1]=-1;
	}

	int z9=0,w9=0,u9=0,x9=0,g9=0,i9=0;


	for(i1=0;i1<size1;i1++){	
	if(input[i1]=='I'){
		i9++;
	}}

	for(i1=0;i1<size1;i1++){
		if(arr[i1]==-1){

		if(input[i1]=='Z'){
			z9++;
			arr[i1]=1;

			for(i3=0;i3<size1;i3++){

				if(arr[i3]==-1){
					if(input[i3]=='E'){
						arr[i3]=1; break;
					}
				}
			}

			for(i3=0;i3<size1;i3++){

				if(arr[i3]==-1){
					if(input[i3]=='R'){
						arr[i3]=1;break;
					}
				}
			}

			for(i3=0;i3<size1;i3++){

				if(arr[i3]==-1){
					if(input[i3]=='O'){
						arr[i3]=1;break;
					}
				}
			}

		}else if(input[i1]=='W'){
			w9++;
			arr[i1]=1;

			for(i3=0;i3<size1;i3++){

				if(arr[i3]==-1){
					if(input[i3]=='T'){
						arr[i3]=1;break;
					}
				}
			}

			for(i3=0;i3<size1;i3++){

				if(arr[i3]==-1){
					if(input[i3]=='O'){
						arr[i3]=1;break;
					}
				}
			}

		}else if(input[i1]=='U'){
			u9++;
			arr[i1]=1;

			for(i3=0;i3<size1;i3++){

				if(arr[i3]==-1){
					if(input[i3]=='F'){
						arr[i3]=1;break;
					}
				}
			}

			for(i3=0;i3<size1;i3++){

				if(arr[i3]==-1){
					if(input[i3]=='O'){
						arr[i3]=1;break;
					}
				}
			}

			for(i3=0;i3<size1;i3++){

				if(arr[i3]==-1){
					if(input[i3]=='R'){
						arr[i3]=1;break;
					}
				}
			}

		}else if(input[i1]=='X'){
			x9++;
			arr[i1]=1;

			for(i3=0;i3<size1;i3++){

				if(arr[i3]==-1){
					if(input[i3]=='S'){
						arr[i3]=1;break;
					}
				}
			}

			for(i3=0;i3<size1;i3++){

				if(arr[i3]==-1){
					if(input[i3]=='I'){
						arr[i3]=1;break;
					}
				}
			}

		}else if(input[i1]=='G'){
			g9++;
			arr[i1]=1;

			for(i3=0;i3<size1;i3++){

				if(arr[i3]==-1){
					if(input[i3]=='E'){
						arr[i3]=1;break;
					}
				}
			}

			for(i3=0;i3<size1;i3++){

				if(arr[i3]==-1){
					if(input[i3]=='I'){
						arr[i3]=1;break;
					}
				}
			}

			for(i3=0;i3<size1;i3++){

				if(arr[i3]==-1){
					if(input[i3]=='H'){
						arr[i3]=1;break;
					}
				}
			}

			for(i3=0;i3<size1;i3++){

				if(arr[i3]==-1){
					if(input[i3]=='T'){
						arr[i3]=1;break;
					}
				}
			}
		}
	}

}

	number[0]=z9;
	number[2]=w9;
	number[4]=u9;
	number[6]=x9;
	number[8]=g9;

	/*printf("hello \n0: %d\t2: %d\t4: %d\t6: %d\t8: %d\n\n",number[0],number[2],number[4],number[6],number[8]);
	for(i1=0;i1<size1;i1++){
		printf("%d  ", arr[i1]);
		
	}*/

	int f9=0,r9=0,o9=0,s9=0;
	
	for(i1=0;i1<size1;i1++){


		if(arr[i1]==-1){
		
			if(input[i1]=='F'){
				f9++;
				arr[i1]=1;

			  for(i3=0;i3<size1;i3++){

				if(arr[i3]==-1){
					if(input[i3]=='I'){
						arr[i3]=1;break;
					}
				 }
				}
				for(i3=0;i3<size1;i3++){

				if(arr[i3]==-1){
					if(input[i3]=='V'){
						arr[i3]=1;break;
					}
				 }
				}

				for(i3=0;i3<size1;i3++){

				if(arr[i3]==-1){
					if(input[i3]=='E'){
						arr[i3]=1;break;
					}
				 }
				}

			}else if(input[i1]=='R'){
				r9++;
				arr[i1]=1;

				for(i3=0;i3<size1;i3++){
				if(arr[i3]==-1){
					if(input[i3]=='T'){
						arr[i3]=1;break;
					}
				 }
				}

				for(i3=0;i3<size1;i3++){

				if(arr[i3]==-1){
					if(input[i3]=='H'){
						arr[i3]=1;break;
					}
				 }
				}

				for(i3=0;i3<size1;i3++){
				if(arr[i3]==-1){
					if(input[i3]=='E'){
						arr[i3]=1;break;
					}
				 }
				}

				for(i3=0;i3<size1;i3++){

				if(arr[i3]==-1){
					if(input[i3]=='E'){
						arr[i3]=1;break;
					}
				 }
				}

			}else if(input[i1]=='O'){
				o9++;
				arr[i1]=1;

				for(i3=0;i3<size1;i3++){
				if(arr[i3]==-1){
					if(input[i3]=='N'){
						arr[i3]=1;break;
					}
				 }
				}

				for(i3=0;i3<size1;i3++){

				if(arr[i3]==-1){
					if(input[i3]=='E'){
						arr[i3]=1;break;
					}
				 }
				}

			}else if(input[i1]=='S'){
				s9++;
				arr[i1]=1;

				for(i3=0;i3<size1;i3++){
				if(arr[i3]==-1){
					if(input[i3]=='E'){
						arr[i3]=1;break;
					}
				 }
				}

				for(i3=0;i3<size1;i3++){

				if(arr[i3]==-1){
					if(input[i3]=='V'){
						arr[i3]=1;break;
					}
				 }
				}

				for(i3=0;i3<size1;i3++){
				if(arr[i3]==-1){
					if(input[i3]=='N'){
						arr[i3]=1;break;
					}
				 }
				}

				for(i3=0;i3<size1;i3++){

				if(arr[i3]==-1){
					if(input[i3]=='E'){
						arr[i3]=1;break;
					}
				 }
				}

			}
		}
	}	

	number[5]=f9;
	number[3]=r9;
	number[1]=o9;
	number[7]=s9;
	number[9]=i9-number[8]-number[5]-number[6];

	//printf("check9 : %d \nANS : ",number[9]);

	//printf("Checking...\n");

	//printf("hello2 \n5: %d\t3: %d\t1: %d\t7: %d\t9: %d\n\n",number[5],number[3],number[1],number[7],number[9]);

	/*for(i1=0;i1<=9;i1++){
		printf("for number %d : %d\n",i1,number[i1]);
	}*/

	int ans=0;
	for(int i1=0;i1<=9;i1++){
		
		for(int i2=0;i2<number[i1];i2++){
			ans=ans*10;
			ans+=i1;	
		}
		
	}

	return ans;
}



int main()
{
	typedef long long lg;
	lg times,i,j;
	scanf("%lld",&times);
	
	for(i=0;i<times;i++)
	{
	  char arr[20002];

	  scanf("%s",&arr);
	
	  printf("Case #%lld: ",i+1);   //,cal(arr));
		 //int count=0;
	//printf("cccc :  %d\n\n",strlen(arr));
	  int count11=0;

	  for(int i1=0;i1<strlen(arr);i1++){

		if(arr[i1]=='Z'){
			printf("0");
		}
	}

	int answer=cal(arr);

	if(answer!=0)
	printf("%d\n", cal(arr));
	else{
		printf("\n");
	}

 }

return 0;
}
