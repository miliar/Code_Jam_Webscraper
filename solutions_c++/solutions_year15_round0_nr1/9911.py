#include <iostream>
#include <string>

int main() {
	int ts;
	std::cin>>ts;
	for(int t=1;t<=ts;t++){
	int shy;
	std::cin>>shy;
	int aud[shy+1];
	std::string audlist;
	std::cin>>audlist;
	for(int i=0;i<=shy;i++){aud[i]=(int)(audlist.at(i)-'0');}
	int ans;
	for(int i=0;i<=1000;i++){
		bool flag=true;
		int stand=i+aud[0];
		for(int j=1;j<=shy;j++){
			if(j>stand){flag=false;}
			stand+=aud[j];
		}
		if(flag){ans=i;break;}
	}
	std::cout<<"Case #"<<t<<": "<<ans<<std::endl;
	}
	return 0;
}