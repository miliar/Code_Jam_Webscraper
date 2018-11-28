#include <iostream>
#include <string>
#include <stdint.h>
using namespace std;

int main() 
{
				uint32_t tc = 0;
				cin>>tc;
				for(uint32_t t = 1; t <= tc; t++)
				{
								uint32_t sMax = 0;
								string sArr;
								cin>>sMax;
								cin>>sArr;
								uint32_t clapsSoFar = 0;
								uint32_t menNeeded =0;
								for(size_t i = 0; i < sArr.size(); i++)
								{
												if(clapsSoFar >= sMax) break;
												if(sArr[i] == '0') continue;
												uint32_t count = sArr[i] - '0';
												if(i <= clapsSoFar)	
												{
																clapsSoFar += count;
																continue;
												}
												uint32_t diff = i - clapsSoFar;
												menNeeded += diff;
												clapsSoFar += diff;
												clapsSoFar += count;
								}
								if(clapsSoFar < sMax)
								{
												menNeeded += (sMax - clapsSoFar);
								}		
								cout<<"Case #"<<t<<": "<< menNeeded<<endl;
					}
}
