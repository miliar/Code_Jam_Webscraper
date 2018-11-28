#include <iostream>
#include <algorithm>
using namespace std;

main(){
	int t,a,b,ar[4],i,j,br[4],m,k;
	
	cin>>t;
	k=0;
	while(t--){
		cin>>a;
		k++;
		for(i=0;i<4;i++){

			for(j=0;j<4;j++){
				if(i==a-1)				
				cin>>ar[j];

				else
				cin>>m;
			//	cout<<ar[j];
			}
		}
		cin>>b;
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				if(i==b-1)				
				cin>>br[j];

				else
				cin>>m;
			//	
			}
		}
		
		sort(ar,ar+4);
		sort(br,br+4);

/*		for(i=0;i<4;i++)
		cout<<" "<<ar[i];
		for(i=0;i<4;i++)
		cout<<" "<<br[i];
*/		
		m=-1;
		for(i=0,j=0;i<4&&j<4;){

			//cout<<i<<ar[i]<<" "<<j<<br[j]<<" "<<m<<endl;
			if(ar[i]==br[j]){
			     if(m==-1)
				m=ar[i];
			     else{
				
				m=0;
				break;	
			     }
				i++;
				j++;
			}

			else if(ar[i]<br[j])
					i++;
			else if(ar[i]>br[j])
					j++;

		}

			cout<<"Case #"<<k<<":";
			if(m==-1)
				cout<<" Volunteer cheated!"<<endl;
			else if(m==0)
				cout<<" Bad magician!"<<endl;
			else
				cout<<" "<<m<<endl;

	}

return 0;
}
