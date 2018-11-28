#include<iostream>
#include<vector>
using namespace std;

/*
long int cal(long int no,long int c){
	ar[no]=c;
	if(no==n)
		return c;
		 
		  long int r=0,p = no;
		   while(p!=0){
		   	r=r*10+p%10;
		   	p=p/10;
		   
		   }
		   long int r1 = -1,r2=-1;
		if((ar[r]==-1 || ar[r]>c+1)&&r>12)
			 r1 = cal(r,c+1);
		if(ar[no+1]==-1 || ar[no+1]>c+1)		
			r2 = cal(no+1,c+1);
		if((r1<r2 && r1!=-1) || r2==-1)
			return r1;
		else
			return r2;

}
*/
int main(){
	
	long int t,i1,c,p,r,co;
	cin>>t;
	
	for (i1=1;i1<=t;i1++){
		int n,*ar;
		cin>>n;
		p=1;
		c=1;
		
		ar = new  int[n+1];
		for(int i=0;i<=n;i++)
			ar[i]=-1;
		ar[1]=1;
		vector <long int> list1;
		list1.push_back(p);
		while(1){
		//cout<<"HSKJ"<<endl;
		 co=list1[0];
		 if(co==n){
		 	c= ar[co];
		 	break;
		 }
		 list1.erase (list1.begin()+0);
		 p=co;
//		 		cout<<"HSKJ"<<endl;
			  r=0;
			   while(p!=0){
			   	r=r*10+p%10;
			   	p=p/10;
			   
			   }
//			   		cout<<"HSKJ"<<endl;
		if(r<=n && (ar[r]==-1  && r!=co)) {
			ar[r]=ar[co]+1;
			if(r==n) {c=ar[r];break;}
			list1.push_back(r);
		}
		if(ar[co+1]==-1){
//					   		cout<<"HSKJ"<<endl;
			if((co+1)==n){
				c=ar[co]+1;
				break;}
//			   		cout<<"HSKJ"<<endl;
			ar[co+1]=ar[co]+1;
			list1.push_back(co+1);
//		   		cout<<"HSKJ"<<endl;
			
			}

		
				
//				cout<<co<<" "<<list1[0]<<endl;
		
		}
			cout<<"Case #"<<i1<<": "<<c<<endl;
/*
		while(p<n)
			{co=p; 
			  r=0;
			   while(p!=0){
			   	r=r*10+p%10;
			   	p=p/10;
			   
			   }

			if(r<=n && r > co){
				p=r;
				c++;
//				cout<<r<<" "<<c<<endl;
			}
			else{
				p=co+1;
				c++;		
//				cout<<p<<" "<<c<<endl;
			}
			
			}
		
*/
//		cout<<"Case #"<<i1<<": "<<cal(p,c)<<endl;

	}
	


}

