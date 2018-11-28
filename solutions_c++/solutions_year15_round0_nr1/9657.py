#include<bits/stdc++.h>
#define gc getchar

using namespace std;

 
void fast_read(int *number){
	
	*number=0;
	
	register char currentChar=gc();
	
	while(currentChar<'0'||currentChar>'9') currentChar=gc();
	
	while(currentChar>='0'&&currentChar<='9'){
		
		*number=(*number)*10+currentChar-'0';
		currentChar=gc();
		
	}
	
}
 
static int dp[2][201],totalElements,types;
vector<short> graph[201];
static short nextOne[201][201],label[201],visited[201];
  
int iterativeDP(){
  	
  int i,j,lastTaken,component,option2,ans=10000000;
  	  	
  for(i=0;i<=types;i++)
    dp[0][i]=0;
 
  for(i=1;i<=totalElements;i++){
     
     int now;
     fast_read(&now);
          
     for(j=1;j<=types;j++){
     	
     	
	   component=label[now];  	
  	      	    
  	    lastTaken=j;
  		dp[i&1][j]=10000000;
     	     	
  		if(now<=lastTaken) dp[i&1][j]=dp[(i+1)&1][now];
  		
  		
  		switch(label[lastTaken]==component){
  			
  			case 1 :
  			
  			dp[i&1][j]=min(dp[i&1][j],1+dp[(i+1)&1][lastTaken]); break;
			 
			default :  	
			
  			
  			 option2=nextOne[lastTaken][component];
  		    			    
		     if(option2!=-1&&option2<=lastTaken) 
		      dp[i&1][lastTaken]=min(dp[i&1][lastTaken],1+dp[(i+1)&1][option2]);	
  			
		  }
  		  	      		  	    
	 }
  	  	
  }  
      
  for(i=1;i<=types;i++)
    ans=min(ans,dp[totalElements&1][i]); 
   
  return ans; 
  	
}
 
void bfs(int u,int assign){
	
	visited[u]=1;
	
	queue<int> Q;
	Q.push(u);
	
	while(Q.size()){
		
		int front=Q.front();Q.pop();
		
		//if(ok[front]==0)
		label[front]=assign;
					
		for(int i=0;i<graph[front].size();i++)		
			if(!visited[graph[front][i]]){
				
				Q.push(graph[front][i]);
				visited[graph[front][i]]=1;
				
			}	
		
	}
					
}
 
int main(void){
	
	char str[100000];
	int testCases,i,ok=0,ans=0,L,Case=1;
	
	scanf("%d",&testCases);
	
	for(int k=0;k<testCases;k++){
		
		cin>>L>>str;
			
		for(i=0,ok=0,ans=0;i<=L;i++){
			
			if(ok>=i) ok+=str[i]-48;			
			
			else if(str[i]>'0'){
			
				ans+=i-ok;    
			    ok+=ans+str[i]-48;
			    
			}
			
		}
		
		cout<<"Case #"<<Case++<<": "<<ans<<endl;
		
	}
	
	return 0;
	
}
