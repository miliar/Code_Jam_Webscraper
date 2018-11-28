#include<iostream>
#include<vector>

const unsigned int INF=1000;

int main(){
	unsigned int T;
	std::cin>>T;
	
	for(unsigned int i=0;i<T;++i){
		unsigned int a,b;
		std::vector<bool> Wzor(17,false);
		unsigned int r=INF;
		unsigned int x;
		
		std::cin>>a;
		for(unsigned int p=0;p<4;++p)
			for(unsigned int k=0;k<4;++k){
				std::cin>>x;
				
				if(p+1==a)
					Wzor[x]=true;
			}
		
		std::cin>>b;
		for(unsigned int p=0;p<4;++p)
			for(unsigned int k=0;k<4;++k){
				unsigned int x;
				std::cin>>x;
				
				if(p+1==b&&Wzor[x]){
					if(r==INF)
						r=x;
					else
						r=INF-1;
				}
					
			}
			
		std::cout<<"Case #"<<(i+1)<<": ";
		if(r==INF)
			std::cout<<"Volunteer cheated!"<<"\n";
		else if(r<=16)
			std::cout<<r<<"\n";
		else
			std::cout<<"Bad magician!"<<"\n";
	}
	
	return 0;
}
