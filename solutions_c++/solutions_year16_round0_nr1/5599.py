#include<iostream>
#include<vector>
using namespace std;

bool IfExist(vector<int>&nums,int digital)
{
  for(int i=0;i<nums.size();i++)
  {
    if(digital==nums[i])
    {
      return true;
    }
  }
  return false;
}

long long int count_sheep(vector<int>&nums,long long int N,int iteration)
{
  int cur_num;
  while(nums.size()!=10){
  cur_num=iteration*N;
  if(cur_num==0)
  {
    return -1;
  }
  int digital;
  do{
    digital=cur_num%10;
    if(!IfExist(nums,digital))
    {
      nums.push_back(digital);
    }
    cur_num/=10;
  }while(cur_num!=0);

  iteration+=1;
 }
 return (iteration-1)*N;
}

int main()
{

  long long int number;
  vector<int>nums;
  int test_case=1;
  int test_input;
  cin>>test_input;
  for(int i=0;i<test_input;i++){
    cin>>number;
    int last_num=count_sheep(nums,number,1);
    if(last_num==-1){
     cout<<"Case #"<<test_case<<": INSOMNIA"<<endl;
   }else{
     cout<<"Case #"<<test_case<<": "<<last_num<<endl;
   }
   test_case++;
   vector<int>().swap(nums);
}

}
