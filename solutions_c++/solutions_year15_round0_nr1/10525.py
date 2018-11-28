#include <gtest/gtest.h>
#include <boost/log/trivial.hpp>
#include <boost/log/core.hpp>
#include <boost/log/expressions.hpp>

namespace log = boost::log;

GTEST_API_ int main(int argc, char **argv) {
    printf("Running main() from gtest_main.cc\n");
    testing::InitGoogleTest(&argc, argv);
    log::core::get()->set_filter(log::trivial::severity >= log::trivial::trace);
    return RUN_ALL_TESTS();
}
