#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
	    int T;
	        cin >> T;
		    for(int i=0; i<T; ++i) {
			            int M;
				            cin >> M;
					            string s;
						            cin >> s;
							            size_t l = s.length();
								            int ret = 0;
									            int num = 0;
										            for (int j=0; j<l; ++j) {
												                if (num >= j) {
															                num+=static_cast<int>(s[j] - '0');
																	                continue;
																			            }
														            ret += (j-num);
															                num += (j-num) + static_cast<int>(s[j] - '0');
																	        }
											            printf("Case #%d: %d\n", i, ret);
												        }
}
