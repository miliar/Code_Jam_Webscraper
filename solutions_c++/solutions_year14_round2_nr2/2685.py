/*
 * program - desc
 * Copyright (C) 2012  Onur Aslan  <onuraslan@gmail.com>
 * 
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

#include <iostream>

unsigned
calculate (unsigned a, unsigned b, unsigned k)
{
  unsigned i, j, l;
  unsigned c = 0;

  for (i = 0; i < a; ++i) {
    for (j = 0; j < b; ++j) {
      l = i & j;
      if (l < k)
        ++c;
    }
  }

  return c;
}

int main (int argc, char *argv[])
{
  unsigned t;

  std::cin >> t;

  for (unsigned i = 1; i <= t; ++i) {
    unsigned a, b, k;
    std::cin >> a;
    std::cin >> b;
    std::cin >> k;
    std::cout << "Case #" << i << ": " << calculate (a, b, k) << std::endl;
  }

  return 0;
}

