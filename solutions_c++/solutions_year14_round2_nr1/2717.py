#include<iostream>
#include<cstdio>
#include<cstring>
#include<ctime>
#include<cmath>
#include <iomanip>

//#define re
using namespace std;



void sortArray(int nums[], int total) {
int x;
int y;
for(x=0; x<total; x++) {
    for(y=0; y<total-1; y++) {
        if(nums[y]>nums[y+1]) {
            int temp = nums[y+1];
            nums[y+1] = nums[y];
            nums[y] = temp;
        }
    }
}
}



double findMedian(int nums[], int total) {
    int temp;
    int i,j;
    for(i=0;i<total;i++)
        for(j=i+1;j<total;j++) {
            if(nums[i]>nums[j]) {
                temp=nums[j];
                nums[j]=nums[i];
                nums[i]=temp;
            }
        }
        if(total%2==0) {
            return (nums[total/2]+nums[total/2-1])/2;
        }else{
            return nums[total/2];
        }
}

//int t,n;

int solve(string s[], int n){
int count[n], current[n];
int moves=0;
int done=0;

for(int i=0;i<n;i++)
   current[i]=0;

while(!done){
done=1;	
char c=s[0][current[0]];
   //initialise count to 0
   for(int j=0;j<n;j++){
   	count[j]=0;
   }

for(int i=0;i<n;i++){

   while(current[i]<s[i].length() && s[i][current[i]]==c){
   	count[i]++;
   	current[i]++;
   }
   if(current[i]>=s[i].length())
      current[i]=-1;
   else if(count[i]==0)
      return -1;
}
int sum=0;
for(int i=0;i<n;i++){
	sum+=count[i];
	if(sum>0 &&count[i]<=0)
	   return -1;
}
sortArray(count, n);
int avg=findMedian(count,n);

//cout<<"avg "<<avg<<endl;
for(int i=0;i<n;i++){
	moves+=(avg>count[i]?avg-count[i]:count[i]-avg);
	//cout<<moves<<" ";
	//cout<<"i="<<i<<" "<<count[i]<<" ";
}


//cout<<endl;
for(int i=0;i<n;i++){
	if(current[i]!=-1)
		done=0;
}
}
return moves;
}


int main(int argc, char const *argv[])
{
#ifdef re
freopen("input.txt","r",stdin);
freopen("output_max.txt","w",stdout);
freopen("log.txt","w",stderr);
#endif
int t,n,k=0;
cin>>t;
while(t-->0){
	k++;
	cin>>n;
	string s[n];
	for(int i=0;i<n;i++){
		cin>>s[i];
	}
	int r=solve(s,n);
	cout<<"Case #"<<k<<": ";
	if(r<0)
	   cout<<"Fegla Won"<<endl;
	 else
	    cout<<r<<endl;
	    
}

    	
/*#ifdef re
printf("\n  Time Taken  %.31f sec\n",(double)clock()/(CLOCKS_PER_SEC));

#endif*/
return 0;
}


