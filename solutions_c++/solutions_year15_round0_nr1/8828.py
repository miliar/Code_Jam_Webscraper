#include<iostream>
#include<cstdio>
#include<cstring>
//#include<cstdlib>
using namespace std;

int main(){
  FILE *fw,*fr;
  fw=fopen("output/file1.txt","w");
  fr=fopen("input/A-large.in","r");
  int t,s_max,i,test_cases;
  unsigned long long sum,count,temp;
  fscanf(fr,"%d",&t);
  test_cases=t;
  while(t--){
    fscanf(fr,"%d",&s_max);
    char str[s_max+1];
    fscanf(fr,"%s",&str[0]);
    sum=0;
    count=0;
    for(i=0;i<=s_max;i++){
      if(sum<i){
	temp=i-sum;
	sum+=temp;
	count+=temp;
      }
      sum+=(int)str[i]-48;
    }
    fprintf(fw,"Case #%d: %llu\n",test_cases-t,count);
  }
  fclose(fw);
  fclose(fr);
  return 0;
}
