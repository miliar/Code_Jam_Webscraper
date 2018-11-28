#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#define print(x) printf("%d\n",x)

//fast input output
inline int scan(){
	
	int n = 0 , sign = 0;
	char ch = getchar() ;
	
    while((ch<48 || ch>58 ) && ch!='-')
	  ch = getchar();
	
	if(ch=='-'){
		sign = 1;
		ch = getchar();
	}  	
	while(ch>47 && ch<59){
	   n = (n<<1) + (n<<3) + ch -'0';
	   ch = getchar();	
	}  
    
    if(sign)
      return -n;
      
	  return n;
}

int main(){
	
	int t , n ,i = 0, count , temp , rem , j;
    t = scan();
	j=1;
	while(j<=t){
		
		int a[10] = {0};

		n = scan();
		count=0;
		
		if(n==0){
		    printf("Case #%d: INSOMNIA\n",j);	
		}
		else{
		i=1;
		 while(1){
			temp = n*i;
			while(temp!=0){
				
				rem = temp%10;
				if(!a[rem]){
					a[rem]++;
					count++;
				}
				//printf("value of temp is %d\n",temp);
			    temp = temp/10;
			}
				if(count==10)
			    	break;
			i++;
			
			if(count==10)
			  break;
		 }
		 printf("Case #%d: %d\n",j,n*i);
	    }
		//print(count);
		j++;

	}

}
