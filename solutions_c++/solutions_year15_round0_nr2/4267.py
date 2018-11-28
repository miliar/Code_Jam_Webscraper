# include<bits/stdc++.h>

#define LL long long
#define FIT(i,t) for(i=0;i<t;i++)
#define FIN(i,d) for(i=0;i<d;i++)
#define FIM(i,max) for(i=1;i<=max;i++)
#define FJT(j,t) for(j=0;j<t;j++)
#define FJN(j,d) for(j=0;j<d;j++)
#define MAX2(a,b) a>b?a:b
#define MIN2(a,b) a>b?b:a
#define REP(i,a,b) for(i=a;i<=b;i++)

using namespace std;

int main(){
	int t;
	
	ifstream infile("C:\\Users\\N_NICHOLAS\\Desktop\\B-large.in");
	//ifstream infile("C:\\Users\\N_NICHOLAS\\Desktop\\check.txt");	
	infile>>t;
	//scanf("%d", &t);
	freopen ("C:\\Users\\N_NICHOLAS\\Desktop\\helloworld.txt","w",stdout);
  	//printf ("This sentence is redirected to a file.");
	
	int s = t;
	int testcase = 0;
	long long int output[10000];
	
	while(t--){
		long long int d, p, i, j, div;
		long long int value = 1000000000, count, max=0;
		//scanf("%d", &d);
		infile >> d;
		
		
		long long int arr_a[10000];
		memset(arr_a,0,sizeof(arr_a));
		
		FIN(i, d){
			infile >> arr_a[i];
			max = MAX2(arr_a[i], max);
		}

		FIM(i, max){
			count = 0;
			FIN(j, d){
				div = arr_a[j]/i;
				if(arr_a[j]%i >0){
					div++;
				}
				div--;
				
				count += div;
			}
			
			count += i;
			
			value = MIN2(value, count);
		}
			
		
		
		output[testcase] = value;
		testcase++;
		
		//cout<<"Case #" << testcase <<": "<<value<<endl;
		
	}
	
	for(int i = 0; i<s; i++){
		cout<<"Case #" << (i+1) <<": "<<output[i]<<"\n";
	}
	
	fclose (stdout);
	return 0;
}

