#include<iostream>
#include<algorithm>
using namespace std;
/*

32 64 96 97 98 99



*/
int recur(int arr[110],int start,int end, int level,int m){
    //cout<<" start  : "<<start<<" : end : "<<end<<" :  level : "<<level<<" : m : "<<m<<"\n";
    if(start>end )
    {
    return level;              
    }
    sort(arr+start,arr+end+1);
    
    if(m==1 )
    return end-start+1;
    
    /*cout<<"\narray in recur : \n";
    for(int i=start;i<=end;i++)
    cout<<arr[i]<<" ";
    */int posmin=-1;
    for(int i=start;i<=end;i++)
                if(arr[i]<m)
                posmin=i;
                else
                break;
                
                if(posmin!=-1)
                {
                //consume all smaller moles from 0 to posmin
                for(int i=start;i<=posmin;i++)
                m+=arr[i];              
                start=posmin+1;                
                }
                //cout<<"\n mole size in recur : "<<m;
              
               
               if(arr[start] >= m && start <=end ){
                             // either add new mole with wght m-1 and then consume it and then 
                           
                             int a1=min(recur(arr,start,end,level+1,m+m-1), recur(arr,start,end-1,level+1,m));
                             //int a2=end-start+1;      
                            // cout<<"\n in branch a1 : "<<a1<<" : a2 : "<<a2;    
                            
                            //system("pause");
                             return a1;         
                             }
               else
               return recur(arr,start,end,level,m);
    
    
    
    }


int main(){
    int t;
    cin>>t;
    int a=t;
    while(t--){
                int arr[110],n, m;
                cin>>m>>n;
                for(int i=0;i<n;i++){
                        cin>>arr[i];
                         }
                   
                int ans=recur(arr,0,n-1,0,m);
                cout<<"Case #"<<a-t<<": "<<ans<<"\n";            
            
               
               }    
    
    
}
