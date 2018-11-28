	#include <fstream>
	#include <cstring>
	
	using namespace std;
	
	ifstream in("a.in"); ofstream out("a.out");
	int T, l=1;
	
	int main()
	{
	in>>T;
	while(T--)
	{
	string nums, result; long long numi,numii, memo[10]={}, total = 0; 
	in>>numi;
	if(numi==0) result = "INSOMNIA"; 
	else {
	
		for(long long i =1 ;;i++)
			{
			 numii = i*numi;
			 nums = to_string(numii);
			 
			 for(int j = 0 ; j < nums.size();j++)
			 {
			 	if(memo[nums[j] -'0']== 0) {memo[nums[j] -'0']=1; total++;}
			 }
			if(total == 10) {result = to_string(numii); break;}
			}
		 
		}
		out<<"Case #"<<l<<": "<<result<<endl;
		l++; memset(memo,0,sizeof(memo));
	}
}


