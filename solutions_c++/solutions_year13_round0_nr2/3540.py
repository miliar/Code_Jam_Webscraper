/*
 * B.cpp
 *
 *  Created on: 2013-4-13
 *      Author: york
 */

#include<iostream>
using namespace std;

int main(){
	int T;
	int N,M;
	int table[100][100];
	int sort[101];
	bool flag;
	bool terminalflag;
	cin >> T;
	for(int tablenum=1;tablenum<=T;++tablenum){
		cin >> N >> M;

		//init
		for(int i=0;i<=100;++i){
			sort[i] = 0;
		}

		terminalflag = true;
		for(int i=0;i<N;++i)
			for(int j=0;j<M;++j){
				cin >> table[i][j];
				sort[table[i][j]] = 1;
			}

		for(int i=0;i<=100 && terminalflag;++i){
			if(sort[i] == 0){
				continue;
			}
			else{
				for(int j=0;j<N && terminalflag;++j)
					for(int k=0;k<M && terminalflag;++k){
						flag = true;
						if(table[j][k] == i){
							for(int col=0;col<N;++col){
								if(table[col][k] > i){
									flag = false;
									break;
								}
							}
							if(flag){
								for(int col=0;col<N;++col)
									table[col][k] = 0;
							}
							else{
								flag = true;
								for(int col=0;col<M;++col){
									if(table[j][col] > i){
											flag = false;
											break;
									}
								}
								if(flag){
									for(int col=0;col<M;++col)
										table[j][col] = 0;
								}
								else{
									terminalflag = false;
									break;
								}
							}
						}

					}
			}
		}
		if(terminalflag){
			cout << "Case #" << tablenum <<": YES" << endl;
		}
		else{
			cout << "Case #" << tablenum <<": NO" << endl;
		}

	}

}

