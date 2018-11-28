    #include<cstdio>
    #include<algorithm>
     
    using namespace std;
     
    int TC,N;
    pair<float,int> Data[1000],Data2[1000];
     
    int a,b,c,status;
    int War,DWar;
    int war(){
    	int res = 0;
    	sort(Data, Data + N);
    		sort(Data2, Data2 + N);
    		for(b = 0; b < N; b++)
    		{
    			status = 0;
    			for(c = 0; c < N; c++)
    			{
    				if(Data[b].first < Data2[c].first && Data2[c].second == 0)
    				{
    					status = 1;
    					Data2[c].second = 1;
    				break;
    				}
    			}
    			if(!status) res++;
    		}
    		return res;
    }
    
    int dwar(){
    	
    	
    }
    int main()
    {
    scanf("%d",&TC);
    for(a = 1; a <= TC; a++)
    	{
    		War = 0;
    		DWar = 0;
    		scanf("%d",&N);
     		for(b = 0; b < N; b++)
    		{
    			scanf("%f",&Data[b].first);
    			Data[b].second = 0;
    		}
     
			for(b = 0; b < N; b++)
    		{
    			scanf("%f",&Data2[b].first);
    			Data2[b].second = 0;
    		}
     
   	War = war();
    for(b=0;b<N;b++){
    	Data[b].second = 0;
    	Data2[b].second = 0;
    }
    for(b = 0; b < N; b++)
    	{
    		status = 0;
    		for(c = 0; c < N; c++)
    		{
    			if(Data[b].first > Data2[c].first && Data2[c].second == 0)
    			{
				    			status = 1;
								Data2[c].second = 1;
    							DWar++;
    							break;
    			}
    		}
    	}
    // Print Untuk War
    printf("Case #%d: %d %d\n",a,DWar,War);
    }
    return 0;
    }
