#include <stdio.h>
#include <string>
#include <string.h>

int main(){
	int nTestCases;
	scanf("%d",&nTestCases);
	for(int i=0;i<nTestCases;++i){
		char str[1002];
		scanf("%s",str);
		std::string outStr;
		outStr.push_back(str[0]);
		#ifdef __DEBUG__
			printf("%s\n",outStr.c_str());	
		#endif
		int lenStr=strlen(str);
		for(int j=1;j<lenStr;++j){
			if(outStr.c_str()[0] <= str[j]){
					outStr = str[j] + outStr;
			}else{
					outStr=outStr+str[j];
			}
			#ifdef __DEBUG__
				printf("%s\n",outStr.c_str());	
			#endif			
		}
		printf("Case #%d: %s\n",i+1,outStr.c_str());
	}
	return 0;
}
