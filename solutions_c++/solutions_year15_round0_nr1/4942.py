# include<bits/stdc++.h>

#define LL long long
#define FIT(i,t) for(i=0;i<t;i++)
#define FIN(i,n) for(i=0;i<n;i++)
#define FJT(j,t) for(j=0;j<t;j++)
#define FJN(j,n) for(j=0;j<n;j++)
#define MAX2(a,b) a>b?a:b
#define MIN2(a,b) a>b?b:a
#define REP(i,a,b) for(i=a;i<=b;i++)

using namespace std;

int main(){
	int t;
	
	ifstream infile("C:\\Users\\N_NICHOLAS\\Desktop\\A-small-attempt1.in");
	//ifstream infile("C:\\Users\\N_NICHOLAS\\Desktop\\check.txt");	
	infile>>t;
	//scanf("%d", &t);
	freopen ("A-small-attempt1.txt","w",stdout);
  	//printf ("This sentence is redirected to a file.");
	
	int s = t;
	int testcase = 0;
	long long int output[10000];
	
	while(t--){
		int n, i, j;
		long long int value = 0;
		//scanf("%d", &n);
		infile >> n;
		
		long long int arr_a[10000];
		memset(arr_a,0,sizeof(arr_a));
		
		
		string s1;
		infile>>s1;
		
		arr_a[0] = (int)s1[0] - 48;
		
		if(n == 0){
			value = 0;
		} else {
		
			for(i = 1; i < s1.length(); i++){
				//scanf("%d", &arr_b[i]);
				arr_a[i] = arr_a[i-1] + ((int)s1[i] -48);
				
				if(((int) s1[i] - 48) > 0){
					if(i > arr_a[i-1]){
						value += i-arr_a[i-1];
						arr_a[i] += value;
					}
				}
			}
			
			for(i = 0; i < s1.length(); i++){
			//	cout<<"Case "<< t<< " Array  :  " <<arr_a[i]<<"  ";
			}
			
			//cout<<endl;
			
		/*	for(i = 0; i < s1.length(); i++){
				if(((int) s1[i] - 48) >0 ){
					if(i > arr_a[i]){
						value += i-arr_a[i] + 1;
					}
				}
			}
			*/
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

