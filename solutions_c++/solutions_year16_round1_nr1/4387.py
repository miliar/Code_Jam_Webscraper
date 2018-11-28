#include "stdio.h"
#include <string.h>
#include "string"
#include "vector"
#include "iostream"
#include "fstream"
using namespace std;


int main(){
	FILE *fp;
	fp = fopen("A-large.in","r");
	ofstream out("The Last Word.txt");
//	out = fopen("The Last Word.txt","w");
	int T;
	fscanf(fp,"%d",&T);
//	scanf("%d",&T);
	for(int tc=0;tc<T;tc++){
		char words[1005],sorts[1005];
		fscanf(fp,"%s",words);
//		scanf("%s",words);		
		vector<char> res;
		int len = strlen(words);
//		printf("%d\n",len);
		res.push_back(words[0]);
		for(int i=1;i<strlen(words);++i){
			if(words[i] < res[0]){
//				printf("back\n");
				res.push_back(words[i]);
			}else{
//				printf("front\n");
				res.insert(res.begin(),words[i]);
			}
		}
//		printf("HELLO\n");
		vector<char>::iterator it;
		printf("Case #%d: ",tc+1);
//		fprintf(out,"Case #%d: ",tc+1);
		out<<"Case #"<<tc+1<<": ";
		int count = 0;
		for(it = res.begin();it<res.end();++it){
//			printf("HELLO\n");
//			printf("%c",it);
			cout<<*it;
			out << *it;
		}
		cout<<endl;
		out<<endl;
	}
}
