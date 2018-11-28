#include<bits/stdc++.h>
//map<int,char> mp;
using namespace std;
vector<pair<int,char> > vec;
pair<int,char>aa,bb,cc;
int arr[26],n;
/*int check(){
   for(int i=0;i<n;i++) if(arr[i]>0) return 1;
   return 0;
}*/
int main(){
   
   int t;cin>>t;
   int count=0;
   while(t--){
   count++;
   cout<<"Case #"<<count<<": ";
     vec.clear();
      cin>>n;
      //cout<<"dsld";
      for(int i=0;i<n;i++) cin>>arr[i];
      for(int i=0;i<n;i++){
         vec.push_back(make_pair(arr[i],char('A'+i)));
      }
      
      while(true){
         sort(vec.begin(),vec.end());
         aa = vec[n-1];
         bb=vec[n-2];
         cc=vec[n-3];
         
         if(aa.first==0) break;
         
         if(cc.first==0|| n==2){
            if((aa.first-bb.first)>=2) {
               cout<<aa.second<<aa.second<<" ";
               vec[n-1].first-=2;
            }
            else if((aa.first-bb.first)==1){
               cout<<aa.second<<" ";
               vec[n-1].first-=1;
            }
            else if((aa.first-bb.first)==0){
               cout<<aa.second<<bb.second<<" ";
               vec[n-1].first--;
               vec[n-2].first--;
            }
         }
         else{
            if((aa.first-bb.first)>=2) {
               cout<<aa.second<<aa.second<<" ";
               vec[n-1].first-=2;
            }
            else if((aa.first-bb.first)==1){
               cout<<aa.second<<bb.second<<" ";
               vec[n-1].first-=1;
               vec[n-2].first-=1;
            }
            else if((aa.first-bb.first)==0 && cc.first==1){
               cout<<cc.second<<" ";
               vec[n-3].first--;
            }
            else if((aa.first-bb.first)==0){
               cout<<aa.second<<bb.second<<" ";
               vec[n-1].first--;
               vec[n-2].first--;
            }
         }
          
      }
      cout<<endl;
      /*while(check()){
       int count=0;
      int maxi1=0,maxi2=0,ind1=0,ind2=0;
      for(int i=0;i<n;i++){
         if(maxi1<=arr[i]){
            maxi2=maxi1;
            ind2=ind1;
            maxi1=arr[i];
            ind1=i;
         }
         else if(maxi2<=arr[i]){
            maxi2=arr[i];
            ind2=i;
         }
      }
      for(int i=0;i<n;i++) if(arr[i]>0) count++;
      cout<<maxi1<<" "<<maxi2<<endl;
      //return 0;
      if(maxi1!=5000 && maxi2!=5000){
         if((maxi1-maxi2)>=2){
            cout<<char('A'+ind1)<<char('A'+ind1)<<" ";
            arr[ind1]-=2;
         }
         else if((maxi1-maxi2)==1 && count==2){
            cout<<char('A'+ind1)<<" ";
            arr[ind1]--;
         }
         else if((maxi1-maxi2)==1 && count>2){
            cout<<char('A'+ind1)<<char('A'+ind2)<<" ";
            arr[ind1]--;
            arr[ind2]--;
         }
         else if((maxi1-maxi2)==0 && count==2){
            cout<<char('A'+ind1)<<char('A'+ind2)<<" ";
            arr[ind1]--;
            arr[ind2]--;
         }
         else if((maxi1-maxi2)==0 && count=>2){
            cout<<char('A'+ind1)<<char('A'+ind2)<<" ";
            arr[ind1]--;
            arr[ind2]--;
         }
         
      }
      return 0;
   }
      cout<<endl;*/
      
   }
   
   
   return 0;
}
