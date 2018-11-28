#include<iostream>
#include<string.h>
#include<math.h>
#include<vector>
using namespace std;

long long isPrime (long long num)
{
    if (num <=1)
        return 0;
    else if (num == 2)         
        return 1;
    else if (num % 2 == 0)
        return 2;
    else
    {
        long long prime = 1;
        long long divisor = 3;
        double num_d = static_cast<double>(num);
        long long upperLimit = static_cast<long long>(sqrt(num_d) +1);
        
        while (divisor <= upperLimit)
        {
            if (num % divisor == 0){
                prime = 0;
                return divisor;
            }
            divisor +=2;
        }
        return prime;
    }
}



vector<long long> numgen(int n,long long arr[]){
	vector<long long> v;
	for(int r=n;r<=n;r++){
  		long long sum;
  		int c=0,p=0;
  		long long add;
  		while(c<r){
  		for(p=0;(p+c)<r;p++){
  			add=0;
  			sum=0;
  			for(int s=0;s<=c;s++){
  				add+=arr[p+s];
  			}
  			sum=arr[r]+add;
  			//cout<<sum<<endl;
  			v.push_back(sum);
  			
  		}
    	  	c++;
		}
	}
return v;
}




int main(){
vector<long long> vec;

long long arr[20];
  arr[0]=10;
  for(int q=1;q<18;q++){
  	arr[q]=arr[q-1]*10;
  }
  
  
  
	int t,n,j;
	cin>>t;
	cout<<"Case #1:"<<endl;
	cin>>n>>j;
	long long sn=pow(10,n-1)+1;
	
	string str=to_string(sn);
	vec=numgen(n-2,arr);
	
	//cout<<"String: "<<str<<endl;
	int len=vec.size();
	//cout<<"size: "<<len<<endl;
	
	int z=0;
while(j--){

//cout<<"Enter loop"<<endl;
	label: long long a[9]={0};
	str=to_string(sn);
	sn=vec[z]+1;
	z++;
	for(int k=2;k<=10;k++){
	
		long long i = stoll(str, nullptr, k);
		//cout<<i<<endl;
		long long ret=isPrime(i);
	//	cout<<"returned from Prime: "<<ret<<endl;
		if(ret==1){
		//cout<<"enter if"<<endl;
			goto label;
		}
		//cout<<"out of if"<<endl;
		a[k-2]=ret;
	}
	//cout<<"out of for"<<endl;
	cout<<str<<" "<<a[0]<<" "<<a[1]<<" "<<a[2]<<" "<<a[3]<<" "<<a[4]<<" "<<a[5]<<" "<<a[6]<<" "<<a[7]<<" "<<a[8]<<endl;

}

return 0;
}
