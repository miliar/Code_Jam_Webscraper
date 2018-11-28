#include<iostream>
#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<vector>
#include<algorithm>
#include<set>
#include<map>
#include<string>
#include<sstream>

#define MOD 1000000007
#define LL long long
#define ULL unsigned long long
#define RESET(a, b) memset(a,b,sizeof(a))

//CoinJamC16

using namespace std;

ULL mx = 511111111;
bool arr[511111111];
int prime(){
	
	ULL count = 1;	

	for(ULL i = 0; i < mx; ++i)
		arr[i] = true;

	ULL sqmax = sqrt(mx);
	//sqmax = mx;
	for(ULL i = 2; i < mx-1; )
	{
		if(count == sqmax)
		{
			//std::cout<<i;
			break;
		}
		//mark all multiples
		for(ULL j = 2; (j*i) < mx-1; ++j)
		{
			arr[i*j] = false;
		}
		//find next prime
		for(ULL k = i+1; k < mx-1; k++)
		{
			if(arr[k])
			{				
				i=k;
				++count;
				break;
			}	
		}
	}
}

ULL checkPrime(ULL val){
	ULL nsqrt = sqrt(val);
	ULL i;
	for(i=2;i<=nsqrt;)
	{
		if(arr[i] == 1){
			if(val%i == 0)
			{
				//isp = false;
				//cout<<i<<" - ";
				break;
			}	
		}
		
		if(i==2)
			i++;
		else
			i+=2;
	}
	
	if(i >= nsqrt)
		return 0;
	else
		return i;
}

int main(){
	std::ios_base::sync_with_stdio(false);
	#ifndef ONLINE_JUDGE
	freopen("inputC.txt","r",stdin);
	#endif
	freopen("outputC.txt","w",stdout);

	ULL i, j, k, n, cases, t;
	ULL N, J;
	cin>>cases;
	
	for(k=1;k<=cases;k++){
		cin>>N>>J;
		//N = 6;
		//J = 3;
		
		//string str = "100011";
		/*
		string str = "1";
		for(i=0;i<N-2;i++)
			str	+= '0';
		str+= '1';
		
		for(i=2;i<=10;i++){
			n=0;
			for(j=0;j<N;j++){
				if(str[j] == '1')
					n += pow(i,N-j-1);
			}
			
			cout<<n<<" ";
		}
		*/
		
		//cout<<"Case #"<<k<<": "<<n<<endl;		
	}
	//cout<<endl;
	cout<<"Case #1:\n";
	
	//int my[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1};
	set<ULL> nums;
	t = 1;
	int z = 0;
	for(i=0;i<N-2;i++){
		vector<int> my;
		for(j=0;j<N-2;j++){
			if(N-2 - j > t)
				my.push_back(0);
			else
				my.push_back(1);
		}
		t++;
		
		do {
			ULL cnum = 0;
			for(j=0;j<N-2;j++)
	    	{
	    		cnum += my[j] * pow(10,j);
	    		//cout << my[j] << ' ';	
			}
			nums.insert(cnum);
			//cout<<'\n';
			z++;
	  	} while ( next_permutation(my.begin(),my.end()) );
		
	}
	//cout<<z<<","<<nums.size();
  	
  	vector <pair<ULL,ULL> > sol;
  	//return 0;
  	//generate primes
  	prime();
  	
  	vector<ULL> vec(nums.begin(), nums.end());
  	
  	ULL num = 2111113111111111;
  	z = 0;
  	for(j=0;j<vec.size();j++){
	  	sol.clear();
	  	
		num = 1000000000000000;
  		if(N == 6)
	  		num = 100000;
	  		
		num += vec[j] * 10 + 1;
		//cout<<num<<" ";
		
		ULL fact = checkPrime(num);
		if(fact == 0)
			continue;
		else
			sol.push_back(make_pair(num, fact));
			//cout<<fact<" ";
		
		for(int i=2;i<10;i++){
			n=0;
    		std::ostringstream ss;
			ss << num;
			string str = ss.str();
			
			for(k=0;k<N;k++){
				if(str[k] == '1')
					n += pow(i,N-k-1);
			}
			
			
			fact = checkPrime(n);
			if(fact == 0)
			{
				break;
			}	
			else
				sol.push_back(make_pair(n, fact));
				//cout<<fact<<" ";
			//cout<<n<<" ";
		}		
		
		if(sol.size() == 9)
		{
			cout<<sol.at(0).first<<" ";
			for(k=1;k<9;k++)
				cout<<sol.at(k).second<<" ";//<<sol.at(k).first<<",";
			cout<<sol.at(0).second<<endl;
			
			z++;
			if(z == J)
				break;
		}	
		//if(isp) z++;
	  	//cout<<":: "<<isp<<endl;
	  	
	}
	//cout<<endl;
	//cout<<z<<"<---";
	
	//for(i=0;i<9;i++)
	//	cout<<sol.at(i).first<<":"<<sol.at(i).second<<endl;
return 0;
}

