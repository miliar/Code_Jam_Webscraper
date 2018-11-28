#include<cstdlib>
#include<cstring>
#include<fstream>
#include<iostream>
using namespace std;

int main()
{
	char a[4][4];
	char *ans[]={"O won", "X won", "Draw", "Game has not completed"};
	int amount, count=0;
	bool notend, end;
	int circle, cross;
	int i, j;
	ifstream infile;
	ofstream outfile;

	infile.open("A-large.in");
	outfile.open("outputA-large.txt");

	infile>>amount;
	while(count++ < amount){
		notend=true, end=false;
		for(i=0; i<4; i++)
			for(j=0; j<4; j++)
				infile>>a[i][j];

		for(i=0; i<4; i++){//row-by-row
			circle=0, cross=0;

			for(j=0; j<4; j++){
				if(a[i][j]=='O' || a[i][j]=='T'){
					circle++;
					if(circle==4){
						outfile<<"Case #"<<count<<": "<<ans[0]<<endl;
						notend=false;
					}
				}

				if(a[i][j]=='X' || a[i][j]=='T'){
					cross++;
					if(cross==4){
						outfile<<"Case #"<<count<<": "<<ans[1]<<endl;
						notend=false;
					}
				}
			}
		}

		if(notend){
			for(j=0; j<4; j++){//column-by-column
				circle=0, cross=0;

				for(i=0; i<4; i++){
					if(a[i][j]=='O' || a[i][j]=='T'){
						circle++;
						if(circle==4){
							outfile<<"Case #"<<count<<": "<<ans[0]<<endl;
							notend=false;
						}
					}

					if(a[i][j]=='X' || a[i][j]=='T'){
						cross++;
						if(cross==4){
							outfile<<"Case #"<<count<<": "<<ans[1]<<endl;
							notend=false;
						}
					}
				}
			}
		}

		if(notend){
			circle=0, cross=0;
			for(i=0, j=0; i<4, j<4; i++, j++){//diagonal
				if(a[i][j]=='O' || a[i][j]=='T'){
					circle++;
					if(circle==4){
						outfile<<"Case #"<<count<<": "<<ans[0]<<endl;
						notend=false;
					}
				}

				if(a[i][j]=='X' || a[i][j]=='T'){
					cross++;
					if(cross==4){
						outfile<<"Case #"<<count<<": "<<ans[1]<<endl;
						notend=false;
					}
				}

			}
		}
		if(notend){
			circle=0, cross=0;
			for(i=3, j=0; i>=0, j<4; i--, j++){//diagonal
				if(a[i][j]=='O' || a[i][j]=='T'){
					circle++;
					if(circle==4){
						outfile<<"Case #"<<count<<": "<<ans[0]<<endl;
						notend=false;
					}
				}

				if(a[i][j]=='X' || a[i][j]=='T'){
					cross++;
					if(cross==4){
						outfile<<"Case #"<<count<<": "<<ans[1]<<endl;
						notend=false;
					}
				}
			}
		}

		if(notend){
			for(i=0; i<4; i++){
				for(j=0; j<4; j++){
					if(a[i][j]=='.'){
						outfile<<"Case #"<<count<<": "<<ans[3]<<endl;
						end=true;
						break;
					}
					else if(i==3 && j==3){
						outfile<<"Case #"<<count<<": "<<ans[2]<<endl;
						end=true;
						break;
					}
				}
				if(end) break;
			}
		}
	}
	infile.close();
	outfile.close();
	/*
	cin>>amount;
	while(count++ < amount){
		notend=true, end=false;
		for(i=0; i<4; i++)
			for(j=0; j<4; j++)
				cin>>a[i][j];

		for(i=0; i<4; i++){//row-by-row
			circle=0, cross=0;

			for(j=0; j<4; j++){
				if(a[i][j]=='O' || a[i][j]=='T'){
					circle++;
					if(circle==4){
						cout<<"Case #"<<count<<": "<<ans[0]<<endl;
						notend=false;
					}
				}

				if(a[i][j]=='X' || a[i][j]=='T'){
					cross++;
					if(cross==4){
						cout<<"Case #"<<count<<": "<<ans[1]<<endl;
						notend=false;
					}
				}
			}
		}
		if(notend){
			for(j=0; j<4; j++){//column-by-column
				circle=0, cross=0;

				for(i=0; i<4; i++){
					if(a[i][j]=='O' || a[i][j]=='T'){
						circle++;
						if(circle==4){
							cout<<"Case #"<<count<<": "<<ans[0]<<endl;
							notend=false;
						}
					}

					if(a[i][j]=='X' || a[i][j]=='T'){
						cross++;
						if(cross==4){
							cout<<"Case #"<<count<<": "<<ans[1]<<endl;
							notend=false;
						}
					}
				}
			}
		}

		if(notend){
			circle=0, cross=0;
			for(i=0, j=0; i<4, j<4; i++, j++){//diagonal
				if(a[i][j]=='O' || a[i][j]=='T'){
					circle++;
					if(circle==4){
						cout<<"Case #"<<count<<": "<<ans[0]<<endl;
						notend=false;
					}
				}

				if(a[i][j]=='X' || a[i][j]=='T'){
					cross++;
					if(cross==4){
						cout<<"Case #"<<count<<": "<<ans[1]<<endl;
						notend=false;
					}
				}

			}
		}

		if(notend){
			circle=0, cross=0;
			for(i=3, j=0; i>=0, j<4; i--, j++){//diagonal
				if(a[i][j]=='O' || a[i][j]=='T'){
					circle++;
					if(circle==4){
						cout<<"Case #"<<count<<": "<<ans[0]<<endl;
						notend=false;
					}
				}

				if(a[i][j]=='X' || a[i][j]=='T'){
					cross++;
					if(cross==4){
						cout<<"Case #"<<count<<": "<<ans[1]<<endl;
						notend=false;
					}
				}
			}
		}

		if(notend){
			for(i=0; i<4; i++){
				for(j=0; j<4; j++){
					if(a[i][j]=='.'){
						cout<<"Case #"<<count<<": "<<ans[3]<<endl;
						end=true;
						break;
					}
					else if(i==3 && j==3){
						cout<<"Case #"<<count<<": "<<ans[2]<<endl;
						end=true;
						break;
					}
				}
				if(end) break;
			}
		}
	}*/
	return 0;
}