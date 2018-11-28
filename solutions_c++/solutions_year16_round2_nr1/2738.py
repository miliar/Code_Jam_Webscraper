#include <cstdlib>
#include <string>
#include <iostream>
#include <math.h>
#include <vector>

using namespace std;



void BubbleSort(int* A, int N){

int i, j;

for (i = 0; i < N; i++)

for (j = i + 1; j < N; j++)

if (A[j] < A[i])

{

int buff;

buff = A[i];

A[i] = A[j];

A[j] = buff;

}

}

int main() {
	int test;
	cin >> test;
	int n;
	for (n = 0; n < test; n++) {
		cout<<"Case #"<<(n + 1)<<": ";
		string t;
		cin >> t;
		int v = t.length();
		char * a = (char*) malloc( v * sizeof(char));



		int * k = (int*) malloc(v * sizeof (int));

		int w = 0;

		int i;

		for (i = 0; i < v; i++) {
			a[i] = t.at(i);
		}


		for (i = 0; i < v; i++) {
			if (a[i] == 'Z') {
				a[i] = '~';
				int t;
				for (t = 0; t < v; t++) {
					if (a[t] == 'E') {
						a[t] = '~';	
						break;					
					}
				}
				for (t = 0; t < v; t++) {
					if (a[t] == 'R') {
						a[t] = '~';	
						break;					
					}
				}
				for (t = 0; t < v; t++) {
					if (a[t] == 'O') {
						a[t] = '~';
						break;						
					}
				}

				k[w] = 0;
				w++;
			}
		}

				for (i = 0; i < v; i++) {


			if (a[i] == 'U') {
				a[i] = '~';
				int t;

				for (t = 0; t < v; t++) {
					if (a[t] == 'F') {
						a[t] = '~';
						break;						
					}
				}

				for (t = 0; t < v; t++) {
					if (a[t] == 'O') {
						a[t] = '~';
						break;						
					}
				}
				for (t = 0; t < v; t++) {
					if (a[t] == 'R') {
						a[t] = '~';
						break;						
					}
				}

				k[w] = 4;
				w++;
			}
		}

				for (i = 0; i < v; i++) {



			if (a[i] == 'F') {
				a[i] = '~';

				int t;

				for (t = 0; t < v; t++) {
					if (a[t] == 'I') {
						a[t] = '~';
						break;						
					}
				}

				for (t = 0; t < v; t++) {
					if (a[t] == 'V') {
						a[t] = '~';
						break;						
					}
				}
				for (t = 0; t < v; t++) {
					if (a[t] == 'E') {
						a[t] = '~';
						break;						
					}
				}

				k[w] = 5;
				w++;
			}
		}


				for (i = 0; i < v; i++) {



			if (a[i] == 'X') {
				a[i] = '~';
				int t;

				for (t = 0; t < v; t++) {
					if (a[t] == 'S') {
						a[t] = '~';
						break;						
					}
				}

				for (t = 0; t < v; t++) {
					if (a[t] == 'I') {
						a[t] = '~';
						break;						
					}
				}
				

				k[w] = 6;
				w++;
			}
		}


				for (i = 0; i < v; i++) {


			if (a[i] == 'V') {
				a[i] = '~';
				int t;

				for (t = 0; t < v; t++) {
					if (a[t] == 'S') {
						a[t] = '~';
						break;						
					}
				}

				for (t = 0; t < v; t++) {
					if (a[t] == 'E') {
						a[t] = '~';
						break;						
					}
				}
				for (t = 0; t < v; t++) {
					if (a[t] == 'E') {
						a[t] = '~';
						break;						
					}
				}

				for (t = 0; t < v; t++) {
					if (a[t] == 'N') {
						a[t] = '~';
						break;						
					}
				}

				k[w] = 7;
				w++;
			}

		}

				for (i = 0; i < v; i++) {


			if (a[i] == 'G') {
				a[i] = '~';
				int t;

				for (t = 0; t < v; t++) {
					if (a[t] == 'E') {
						a[t] = '~';
						break;						
					}
				}

				for (t = 0; t < v; t++) {
					if (a[t] == 'I') {
						a[t] = '~';
						break;						
					}
				}
				for (t = 0; t < v; t++) {
					if (a[t] == 'H') {
						a[t] = '~';
						break;						
					}
				}

				for (t = 0; t < v; t++) {
					if (a[t] == 'T') {
						a[t] = '~';
						break;						
					}
				}

				k[w] = 8;
				w++;
			}

		}



		for (i = 0; i < v; i++) {


			if (a[i] == 'I') {

				a[i] = '~';
				int t;

				for (t = 0; t < v; t++) {
					if (a[t] == 'N') {
						a[t] = '~';
						break;						
					}
				}

				for (t = 0; t < v; t++) {
					if (a[t] == 'N') {
						a[t] = '~';
						break;						
					}
				}
				for (t = 0; t < v; t++) {
					if (a[t] == 'E') {
						a[t] = '~';
						break;						
					}
				}

				

				k[w] = 9;
				w++;
			}

		}


		for (i = 0; i < v; i++) {

			if (a[i] == 'N') {

				a[i] = '~';
				int t;

				for (t = 0; t < v; t++) {
					if (a[t] == 'O') {
						a[t] = '~';
						break;						
					}
				}

				
				for (t = 0; t < v; t++) {
					if (a[t] == 'E') {
						a[t] = '~';
						break;						
					}
				}

				

				k[w] = 1;
				w++;
			}

		}


						for (i = 0; i < v; i++) {


			if (a[i] == 'W') {
				a[i] = '~';
				int t;

				for (t = 0; t < v; t++) {
					if (a[t] == 'T') {
						a[t] = '~';
						break;						
					}
				}

				for (t = 0; t < v; t++) {
					if (a[t] == 'O') {
						a[t] = '~';
						break;						
					}
				}
				

				

				k[w] = 2;
				w++;
			}

		}

						for (i = 0; i < v; i++) {


			if (a[i] == 'R') {
				a[i] = '~';
				int t;

				for (t = 0; t < v; t++) {
					if (a[t] == 'T') {
						a[t] = '~';
						break;						
					}
				}

				for (t = 0; t < v; t++) {
					if (a[t] == 'H') {
						a[t] = '~';
						break;						
					}
				}
				for (t = 0; t < v; t++) {
					if (a[t] == 'E') {
						a[t] = '~';
						break;						
					}
				}

				for (t = 0; t < v; t++) {
					if (a[t] == 'E') {
						a[t] = '~';
						break;						
					}
				}

				
				k[w] = 3;
				w++;
			}

		}

		BubbleSort(k, w);
		for (i = 0; i < w; i++) {
			cout<<k[i];
		}

		cout<<endl;




		}

	}