#include<cstdio>
#include<iostream>
#include<string>
#define MAX 1005
using namespace std;

int main(){    
    
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    
    int testCases,count=1;
    string input;
    cin>>testCases;
        
    while(testCases--){
        
        int tmp;
        cin>>tmp;
        cin>>input;
        int sumSoFar [MAX], requiredFriends = 0;
        
        sumSoFar[0]=input[0]-'0';
        
        for(int i=1;i<input.size();i++){    
            sumSoFar[i] = sumSoFar[i-1] + input[i]-'0';
            
            if(sumSoFar[i-1] < i && (input[i]-'0') != 0 ){
                int requiredAdditions = i-sumSoFar[i-1];
                requiredFriends += requiredAdditions;
                sumSoFar[i] =  sumSoFar[i] + requiredAdditions;
            }
        }
        
        cout<<"Case #"<<count<<": "<<requiredFriends<<endl;
        count++;
    }
    
 return 0;   
}
