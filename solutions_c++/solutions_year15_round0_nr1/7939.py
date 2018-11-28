#include <iostream>
#include <string>
using namespace std;

int main() {
    int T; 
    cin>>T;
    int test=T;
    while(T--)
    {
        int N; int result=0,count;
        cin>>N;
         string s; 
        cin>>s;
        count = s[0]-'0';
        //cout<<" count "<<count<<"\n";
        for(int i=1;i<=N;i++)
        {
            
            if(s[i]!='0')
            {
                if(count<i)
                {
                    result = result + i-count;
                    count = i+s[i]-'0';
                }
                else 
                 {
                     count = count + s[i]-'0';
            
                 } 
            }
            
            
        }
        if(N==0) 
        {
            result=0;
            cout<<"Case #"<<(test-T)<<":"<<" "<<result<<"\n";
            continue;
        }
       
        
        cout<<"Case #"<<(test-T)<<":"<<" "<<result<<"\n";
    }
	// your code goes here
	return 0;
}
