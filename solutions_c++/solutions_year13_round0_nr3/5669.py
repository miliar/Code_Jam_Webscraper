#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <cmath>
 
int main(void)
{
  int n, t;
  std::cin >> n;

  for (t = 1; t <= n; t++) {
    long long unsigned int a, b, r = 0, s;
    std::cin >> a >> b;

    for (; a <= b; a++) {

      //std::cout << "a=" << a << " b=" << b << std::endl;

      s = sqrt(a);
      if (s * s == a) {
	std::ostringstream ostr;
	ostr << a;
	std::string r_str, str = ostr.str();
	r_str.assign(str);
	std::reverse(str.begin(), str.end());
	if (!str.compare(r_str)) {
	  std::ostringstream ostr;
	  ostr << s;
	  std::string r_str, str = ostr.str();
	  r_str.assign(str);
	  std::reverse(str.begin(), str.end());
	  if (!str.compare(r_str)) {
	    //std::cout << "  " << str << std::endl;
	    r++;
	  }
	}
      }
    }
    std::cout << "Case #" << t << ": " << r << std::endl;
  }

  return 0;
}
